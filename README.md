# Hiring Task 2
## User CRUD App
### Tech
- Python - Language
- FastAPI - Webframework
- MongoDB - DB

## How to run Locally

cd into root directory and install requirements. Create virutal env if necessary.
```sh
pip install -r requirements.txt
```

Setup MongoDB Server
[Follow the official installation guide](https://www.mongodb.com/docs/manual/installation/)
Start mongodb server
```sh
mongo
```
Establishing MongoDB connection in FastAPI
Navigate to app.server.databases.py module
"AsyncIOMotorClient" methods takes mongodb uri as argument

If running MongoDB Locally
```sh
"mongodb://<user>:<password>@<host>:<port>/<dbname>"
```
or
If using MongoDB atlas cluster
```sh
"mongodb+srv://<uri>"
```
Starting the App
Runs the app with uvicorn server
```sh
python app/main.py
```
## How to run as Docker Container
Install Docker Engine by following the official installation [Guide](https://www.mongodb.com/docs/manual/installation/).
cd into the root directory
Using docker compose to pull and build image and building container
```sh
docker-compose up --build
```
or start in detached mode without interactive shell
```sh
docker-compose up -d
```

If everthing went correct we will see following message at the end
```sh
$ Application startup complete.
```
## How to use the APIs:
FastAPI provides web interface to use the APIs, also can be used with other API testing tools and curl or dedicated frontend

User http://0.0.0.0:3000/docs/ to open interactive docs provide by FastAPI to try all apis.

##### Create User
http://0.0.0.0:3000/user/
###### Method: POST
id and created_at field are optional since they have auto default value functions
Request Body
```sh
{
  "_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "John Doe",
  "email": "johndoe@gmail.com",
  "created_at": "2023-11-12T21:02:34.912Z"
}
```

##### GET User List
Returns all the users details 
http://0.0.0.0:3000/user/
###### Method: GET
Response
```sh
[
  {
    "_id": "8ca1f642-1422-4ebf-ac7d-36c8f4dbc227",
    "name": "strifadfdfng",
    "email": "stradfadfing@yahoo.com",
    "created_at": "2023-11-12T19:34:23.829000"
  },
  {
    "_id": "df9146bc-21a1-4ffd-83f8-be38c44cd00e",
    "name": "string",
    "email": "string@gmail.com",
    "created_at": "2023-11-12T20:13:33.569000"
  }
]
```

##### GET User by id
Returns a single record of user matching the id, returns 404 if id doesn't match any record
http://0.0.0.0:3000/user/{id}
###### Method: GET
Response
```sh
[
  {
    "_id": "8ca1f642-1422-4ebf-ac7d-36c8f4dbc227",
    "name": "strifadfdfng",
    "email": "stradfadfing@yahoo.com",
    "created_at": "2023-11-12T19:34:23.829000"
  }
]
```

##### Update User data by id
Updates a single record of user matching the id, returns 404 if id doesn't match any record
http://0.0.0.0:3000/user/{id}
We update can update only name and email fields since id and created_at fields need to unchanged after creation.
###### Method: Put
Request
```sh
[
  {
    "name": "strifadfdfng",
    "email": "stradfadfing@yahoo.com"
  }
]
```

##### Delete User data by id
Deletes a single record of user matching the id, returns 404 if id doesn't match any record
http://0.0.0.0:3000/user/{id}
###### Method: Delete
Response
```sh
{"message": "User deleted successfully"}
```

###### Additional Info:
The docker-compose file can be further improved by adding .env and importing config details from env.





