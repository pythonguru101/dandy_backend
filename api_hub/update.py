import os
import subprocess
import tarfile
import shutil
import json

from distutils.version import StrictVersion


def checkForUpdate():
    current_version = "0.0.0"
    with open("/home/mendel/projects/dandy_software/version.txt", "r") as file:
        current_version = file.read().rstrip()

    print("Current version: " + current_version)

    # get available versions
    command = "curl -X GET http://34.150.168.90:1818/get_updates -H 'Content-Type:application/json'"
    output = subprocess.check_output(command.split(" "))
    lines  = json.loads(output)

    versions = []
    for line in lines:
        tokens = line.split(" ")
        version = tokens[-1].replace(".tar.xz", "")
        versions.append(version)

    versions.append(current_version)
    versions.sort(key=StrictVersion)  # sort versions, including current version

    current_version_index = max(loc for loc, val in enumerate(versions) if val == current_version)

    if versions[-1] == current_version:
        print("Up to date")
        still_updating = False
        return None

    print("Update available")
    next_version = versions[current_version_index + 1]
    return next_version


def downloadUpdate():
    next_version = checkForUpdate()
    if next_version is None:
        return

    print("Starting download")

    # empty update folder
    update_folder = "/home/mendel/updates/"
    if os.path.exists(update_folder):
        shutil.rmtree(update_folder)
    os.makedirs(update_folder)

    # download next version
    encrypted_tarball_filepath = update_folder + next_version + ".bin"
    command = "curl -X GET http://34.150.168.90:1818/download_update/" + next_version + ".tar.xz --output " + encrypted_tarball_filepath
    subprocess.call(command.split(" "))

    # decrypt
    decrypted_tarball_filepath = update_folder + next_version + ".tar.xz"
    command = "openssl enc -aes-256-cbc -md sha512 -pbkdf2 -iter 100000 -salt -k fordandyroboteyesonly -d -in "  + encrypted_tarball_filepath + " -out " + decrypted_tarball_filepath
    subprocess.call(command.split(" "))

    # unpack new version
    with tarfile.open(decrypted_tarball_filepath) as f:
        f.extractall(update_folder)

    # remove tarballs
    os.remove(encrypted_tarball_filepath)
    os.remove(decrypted_tarball_filepath)

    print("Download and extraction done")
    return True


def applyDownloadedUpdate():
    # check for downloaded version
    update_folder = "/home/mendel/updates/"
    updates = os.listdir(update_folder)
    if len(updates) == 0:
        print("No update to apply")
        return

    new_version_path = update_folder + updates[0]

    print(new_version_path)

    # stop current operations
    command = "sudo systemctl stop ros_launch.service"
    subprocess.call(command.split(" "))

    # run pre-install
    preinstall_path = new_version_path + "/pre_install.sh"
    if os.path.exists(preinstall_path):
        command = "sudo bash " + preinstall_path
        subprocess.call(command.split(" "))

    print("pre-install done")

    # backup old version
    backup_dir = "/home/mendel/projects/dandy_software_backup"
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    os.rename("/home/mendel/projects/dandy_software", backup_dir)

    print("backup done")

    # move new version in place
    os.rename(new_version_path, "/home/mendel/projects/dandy_software")

    print("move done")

    # run post install
    postinstall_path = new_version_path + "/post_install.sh"
    if os.path.exists(postinstall_path):
        command = "sudo bash " + postinstall_path
        subprocess.call(command.split(" "))

    print("post install done")

    # move uninstall script
    uninstall_path = new_version_path + "/uninstall.sh"
    if os.path.exists(uninstall_path):
        shutil.copy(uninstall_path, "/home/mendel/projects/dandy_software/scripts/")

    print("Install done, rebooting now")

    # reboot
    command = "sudo reboot now"
    subprocess.call(command.split(" "))


def rollback():
    # Run uninstall script
    uninstall_path = "/home/mendel/projects/dandy_software/scripts/uninstall.sh"
    if os.path.exists(uninstall_path):
        command = "sudo bash " + uninstall_path
        subprocess.call(command.split(" "))

    if os.path.isdir("/home/mendel/projects/dandy_software_backup"):
        shutil.rmtree("/home/mendel/projects/dandy_software")
        shutil.copy("/home/mendel/projects/dandy_software_backup", "/home/mendel/projects/dandy_software")
