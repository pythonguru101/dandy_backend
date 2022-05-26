
##### Prerequisite
1. This project is tested in Ubuntu 20.04.3 LTS
2. Python 3.8.10

##### Installation Guide
1. Create a Directory
```bash
mkdir directory name
cd directory name
```

2. From source:

```bash
git clone https://github.com/example.git
```

3. Create Python Environment:
```bash
python3 -m venv env
```
4. Activate Environment
```bash
source env/bin/activate
```
5. Change Directory
```bash
cd dandy_back_end
```
5. Install requirements.txt
```bash
pip3 install -r requirements.txt
```
6. Run main.py
```bash
python3 -m main
```
7. Open http://127.0.0.1:5000


 ##### Api Details

###### Receiving and storing wifi data to connect with robot

```End Point```: ```/connect-with-robot/``` <br>
```Request Method```: ```Post``` <br>
```Args Example: ```
```
{
   'wifi_connection_data':'127.0.0.1'
}
```

```Sucecessful Response: ```
```
{
   'StatusCode': 200,
   'message': 'Wifi connection data has been successfully stored'
}
```

```Unsuccessful Response: ```
```
{
    'StatusCode': 400,
    'message': 'Wifi connection data is required',
}
```


###### Receiving and storing geofence location data

```End Point```: ```/robot-geofence-location/``` <br>
```Request Method```: ```Post``` <br>
```Args Example: ```
```
{
    'geofence_location':'987545'
}
```

```Sucecessful Response: ```
```
{
    'StatusCode': 200,
    'message': 'Geofence location data has been successfully stored'
}
```

```Unsuccessful Response: ```
```
{
    'StatusCode': 400,
    'message': 'Geofence location data is required',
}
```
