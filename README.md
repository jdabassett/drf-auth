# DRF API with JWT Authentication

## Usage


How to make requests to endpoints.
```python
import requests

reqUrl = "http://localhost:8000/api/<endpoint><int:pk>"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
# for all CRUD operations ONLY
 "Authorization": "Bearer <access_token>", 
 "Content-Type": "application/x-www-form-urlencoded" 
}

payload = "<payload>"

response = requests.request("<method>", reqUrl, data=payload,  headers=headersList)
```

| endpoint                     | action                        | pk    | method | access_token | refresh_token | password & username | payload                                                                        |
|------------------------------|-------------------------------|-------|--------|--------------|---------------|---------------------|--------------------------------------------------------------------------------|
| token/                       | get access and refresh tokens | False | POST   | False        | False         | True                | "password=<password>&username=<username>"                                      |
| token/refresh/               | new access token              | False | POST   | False        | True          | True                | "refresh=<refresh_token>&password=<password>&username=<username>"              |
| v1/snacks/create/            | get request                   | False | GET    | True         | False         | False               | ""                                                                             |
| v1/snacks/create/            | post request                  | False | POST   | True         | False         | False               | json.dumps({"owner": 1, "name": "bananas", "description": "fruit"})            |
| v1/snacks/create/            | put request                   | True  | PUT    | True         | False         | False               | json.dumps({"id":6, "owner": 1, "name": "bananas", "description": "fruities"}) |
| v1/snacks/create/            | delete request                | True  | DELETE | True         | False         | False               | ""                                                                             |
| v1/snacks/collection/create/ | get request                   | False | GET    | True         | False         | False               | ""                                                                             |
| v1/snacks/collection/create/ | post request                  | False | POST   | True         | False         | False               | json.dumps({"owner": 1, "snacks": [3, 2, 1]})                                  |
| v1/snacks/collection/create/ | put request                   | True  | PUT    | True         | False         | False               | json.dumps({"id": 2, "owner": 1, "snacks": [3, 2, 1]})                         |
| v1/snacks/collection/create/ | delete request                | True  | DELETE | True         | False         | False               | ""                                                                             |
