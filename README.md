# DRF API with JWT Authentication

## Author:
Jacob Bassett

## Description: 
This is a small api using Django Rest Framework(DRF), Simple-JWT, and Gunicorn. Jacob built it to practice leveraging these tools to build an rest api.

## Usage:

After cloning this repository down to your local machine run the following commands.
```bash
# create a docker container 
docker compose up -d
# open a shell to create new admin user
docker compose exec web bash
# create a administrative user
python manage.py createsuperuser
Username: admin
Email address: admin@email.com
Password: 1234
Password (again): 1234
Bypass password validation and create user anyway? [y/N]: y
# after finishing all of the following requests, exit the shell by
exit
```

## Testing:

Open Postman, Thunderclient, or use the following python script to make requests to the api. More instructions after table.
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
| token/refresh/               | get new access token          | False | POST   | False        | True          | True                | "refresh=<refresh_token>&password=<password>&username=<username>"              |
| v1/snacks/create/            | get request                   | False | GET    | True         | False         | False               | ""                                                                             |
| v1/snacks/create/            | post request                  | False | POST   | True         | False         | False               | json.dumps({"owner": 1, "name": "bananas", "description": "fruit"})            |
| v1/snacks/create/            | put request                   | True  | PUT    | True         | False         | False               | json.dumps({"id":1, "owner": 1, "name": "bananas", "description": "fruities"}) |
| v1/snacks/create/            | delete request                | True  | DELETE | True         | False         | False               | ""                                                                             |
| v1/snacks/collection/create/ | get request                   | False | GET    | True         | False         | False               | ""                                                                             |
| v1/snacks/collection/create/ | post request                  | False | POST   | True         | False         | False               | json.dumps({"owner": 1, "snacks": [1]})                                        |
| v1/snacks/collection/create/ | put request                   | True  | PUT    | True         | False         | False               | json.dumps({"id": 1, "owner": 1, "snacks": [1]})                               |
| v1/snacks/collection/create/ | delete request                | True  | DELETE | True         | False         | False               | ""                                                                             |


#### Request descriptions:

1. Request: Make a post request to endpoint:'token/' endpoint with username:'admin' and password:'1234'. 
  * Response: Should return refresh and access tokens.


2. Request: Use returned refresh token along with username and password to make a post request to endpoint:'token/refresh'.
  * Response: Should return new access token.

  
3. Request: Use access token to make post request to endpoint:'v1/snacks/create/' along with following json in the body.
```json
{
  "owner": 1,
  "name": "pear",
  "description": "fruit"
}
```
  * Response: Should return record with id, created_at, and updated_at.

4. Request: Use access token to make a get request to the endpoint:'v1/snacks/create/'.
  * Response: Should return list with 'pear' record.

  
5. Request: Use access token to make a put request to the endpoint: 'v1/snacks/create/1' along with the following json in the body.
```json
{
  "owner": 1,
  "name": "apply",
  "description": "fruit"
}
```
  * Response: Should return updated record.

6. Request: Use access token to make a delete request to the endpoint:'v1/snacks/create/1'.
  * Response: Should return '204 No Content'.