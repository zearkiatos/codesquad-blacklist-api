# Description
This is an python 🐍 with flask 🌶️ api to management the blacklist for a company

# Made with
[![Python](https://img.shields.io/badge/python-2b5b84?style=for-the-badge&logo=python&logoColor=white&labelColor=000000)]()
[![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=000000)]()


# Postman documentation 🧑🏻‍🚀🚀

You can check the postman documentation make a clic in the next

[![POSTMAN](https://img.shields.io/badge/postman-ff6c37?style=for-the-badge&logo=postman&logoColor=white&labelColor=000000)](https://documenter.getpostman.com/view/1347256/2sA3Bj7Z4w)

URL: [https://documenter.getpostman.com/view/1347256/2sA3Bj7Z4w](https://documenter.getpostman.com/view/1347256/2sA3Bj7Z4w)

# Prerequirements

* Python 🐍
* Docker & docker-compose 🐳 (Optional).
* For Linux 🐧 and mac 🍎 you can use makefile.
* For Windows 🪟 you can use bash function.

# How to execute

If you want execute without docker then you must execute the next commands in your terminal.
Note: firstable is important that you have your python virtual environmente created.

1. Firstly, you should have the **.env** please follow the file **.env.example** you should have something like this

```txt
FLASK_APP=flaskr/app
FLASK_ENV=development
APP_NAME=codesquad-blacklist-api
SECRET_KEY=[SECRET_KEY]
JWT_SECRET_KEY=[SECRET_KEY]
DATA_BASE_URI=[DATA_BASE_URL]
```
The **.env.dev** for your local environment

```txt
FLASK_APP=flaskr/app
FLASK_ENV=development
APP_NAME=codesquad-blacklist-api
SECRET_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbnZpcm9ubWVudCI6ImRldmVsb3BtZW50IiwiYXBwbGljYXRpb24iOiJjb2Rlc3F1YWQtYmxhY2tsaXN0LWFwaSJ9.yJu4GXzVheB7U4VNFAEc2iElgUYf3UtQErhHDDK2vgo
JWT_SECRET_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbnZpcm9ubWVudCI6ImRldmVsb3BtZW50IiwiYXBwbGljYXRpb24iOiJjb2Rlc3F1YWQtYmxhY2tsaXN0LWFwaSJ9.yJu4GXzVheB7U4VNFAEc2iElgUYf3UtQErhHDDK2vgo
DATA_BASE_URI=postgresql://postgres:postgres@db:5432/blacklist
```

The **.env.db** for your local db environment

```txt
POSTGRES_DB=blacklist
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
PGPORT=5432
```

2. First step you should activate the python environment

```sh
# With Linux 🐧 or Mac 🍎
make activate

# With Windows 🪟
source run.sh; activate

# With python flask 🐍 🌶️
python3 -m venv venv
source venv/bin/activate
```

3. Second step you should install all the dependencies and python 🐍 packages 📦

```sh
# With Linux 🐧 or Mac 🍎
make install

# With Windows 🪟
source run.sh; install

# With python flask 🐍 🌶️
pip install -r requirements.txt
```

4. Finally, into directory flaskr execute

```bash
# With Linux 🐧 or Mac 🍎 you can send a specific port with port=5000 param
make run
#or
make run port=5000

# With Windows 🪟 you can send a specific port with 5000 param
source run.sh; run
# or
source run.sh; run 5000

# With python flask 🐍 🌶️
flask run
```

# How to execute with docker 🐳

1. Step one locate in the root of the project

```bash
cd codsquad-backlist-api
```

2. Run in docker 🐳

```bash
# With Linux 🐧 or Mac 🍎
make docker-dev-up

# Command to run with nginx  and proxy reverse 
make docker-up

# With Windows 🪟
source run.sh; docker_dev_up

# Command to run with nginx  and proxy reverse 
source run.sh; docker_up

# With docker compose for all Operative Systems

docker compose -f=docker-compose.develop.yml up --build

# Command to run with nginx  and proxy reverse

docker compose up --build
```

3. Make sure that all microservices are running

* Executing this command

```bash
    docker ps
```

# Validate API health

You can call the health check, for example:

```sh
$ curl -X GET --location 'http://localhost:5000/health'
```

You must receive a request like next:
```json
{
    "environment": "development",
    "application": "codesquad-blacklist-api",
    "status": 200
}
```