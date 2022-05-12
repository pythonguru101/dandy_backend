import ipapi
from flask import Flask, request, render_template

#pip install ipapi


app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def Index():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    return render_template('index.html', data=data)





if __name__ == '__main__':
    app.debug = True
    app.run()




# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')
#     # return "Hello, World!" 

# @app.route("/products")
# def products():
#     return "this is products page"

# if __name__ == "__main__":
#     app.run(debug=True)
#     # app.run(host="0.0.0.0")
# --------------------------------------------------  
    
# import subprocess

# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# results = results.decode("ascii")
# results = results.replace("\r","")
# ls = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
# print(ssids)    
# # ---------------------------------------------
# import re
# import subprocess
# arp_out =subprocess.check_output(['arp','-lan'])

# re.findall(r"((\w{2,2}\:{0,1}){6})",arp_out)
# # -------------------------------------------
# # from scapy.all import *

# # ans,unans = arping("192.168.0.0/24", verbose=0)
# # for s,r in ans:
# #     print("{} {}".format(r[Ether].src,s[ARP].pdst))
# # ----------------------------------------------
# from who_is_on_my_wifi import *

# WHO = who() # who(n)
# for j in range(0, len(WHO)):
# 	comm = f"\n{WHO[j][0]} {WHO[j][1]}\n{WHO[j][2]} {WHO[j][3]}\n{WHO[j][4]} {WHO[j][5]}\n"
# 	print(comm)

# # >>> OUTPUT <<<

# # IP Address: 192.168.0.1
# # Mac Address: 38:43:7d:62:42:24
# # Device: Compal Broadband Networks, Inc. (router)

# # IP Address: 192.168.0.24
# # Mac Address: 10:5b:ad:6c:64:55
# # Device: Mega Well Limited

# ...
# # -----------------------------------------
# # from who_is_on_my_wifi import *

# dev = device()

# print(f"""
# PC Name:            {dev[0]}
# PC Product-Name:    {dev[1]}
# MAC Address:        {dev[2]}
# IP Address (host):  {dev[3]}
# IP Address:         {dev[4]}
# Public IP:          {dev[5]}
# PC HostName:        {dev[6]}
# WiFi Name:          {dev[7]}
# Gateway:            {dev[8]}
# DNS 1:              {dev[9]}
# DNS 2:              {dev[10]}
# Password:           {dev[11]}
# Security:           {dev[12]}
# Interface:          {dev[13]}
# Frequency:          {dev[14]}
# Signal:             {dev[15]}
# Channel:            {dev[16]}


# Country:            {dev[17]}
# Region:             {dev[18]}
# City:               {dev[19]}
# Zip Code:           {dev[20]}
# Latitude:           {dev[21]}
# Longitude:          {dev[22]}
# Map:                {dev[23]}
# ISP:                {dev[24]}
# """)

