
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

###### Connect with Robot

```End Point```: ```/connect-with-robot``` <br>
```Request Method```: ```Post``` <br>
```Args Example: ```
```
{
    "ssid":"49455",
    "password":"TopSecret"
}
```

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "device": {
        "battery_level": "Highly Charged",
        "connected_ssid": "458940",
        "connection_status": "connected",
        "id": "Abc123",
        "name": "Robot Micro",
        "status": "running",
        "storage_level": "Full",
        "type": "Micro Controller"
    },
    "message": "Successfully connected"
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Password is required"
}
```


###### Fencing Robot Location

```End Point```: ```/robot-location-fencing``` <br>
```Request Method```: ```Post``` <br>
```Args Example: ```
```
{
    "coordinates":[
        {
            "latitude":23.2332,"longitude": 23.2332
        },
        {
            "latitude":23.2332,"longitude": 23.2332
        }
    ],
    "holes":[
        {
            "latitude":23.2332,"longitude": 23.2332
        },
        {
            "latitude":23.2332,"longitude": 23.2332
        }
    ],
    "id":0
}
```

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "coordinates": [
        {
            "latitude": 23.2332,"longitude": 23.2332
        },
        {
            "latitude": 23.2332,"longitude": 23.2332
        }
    ],
    "holes": [
        {
            "latitude": 23.2332,"longitude": 23.2332
        },
        {
            "latitude": 23.2332,"longitude": 23.2332
        }
    ],
    "id": 0,
    "message": "Data successfully stored"
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Valid data is required"
}
```
###### Get Robot Current Location

```End Point```: ```/get-robot-current-location``` <br>
```Request Method```: ```Get``` <br>

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "coordinates": {
        "latitude": 40.73061,
        "longitude": -73.953242
    },
    "device": {
        "battery_level": "Highly Charged",
        "connected_ssid": "458940",
        "connection_status": "connected",
        "id": "Abc123",
        "name": "Robot Micro",
        "status": "running",
        "storage_level": "Full",
        "type": "Micro Controller"
    },
    "malfunction": {
        "clipper": true,
        "motor": true,
        "sensor": true,
        "wheel_1": true,
        "wheel_2": true,
        "wheel_3": true,
        "wheel_4": true
    },
    "message": "Successfully data retreived"
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Raised error"
}
```
###### Check Update

```End Point```: ```/check-update``` <br>
```Request Method```: ```Get``` <br>

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "is_available_update":True
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Raised error"
}
```
###### Update Software

```End Point```: ```/update-software``` <br>
```Request Method```: ```Post``` <br>
```Args Example: ```
```
{
    "is_update_available": True
}
```

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "message": "Software update available data successfully passed"
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "is_update_available field is required"
}
```