import os
from dotenv import load_dotenv

environment = os.getenv('FLASK_ENV')

if environment == 'development' or environment == 'local':
    load_dotenv(dotenv_path='.env.dev')
elif environment == "test":
    load_dotenv(dotenv_path='.env.test')
else:
    load_dotenv(dotenv_path='.env')


class Config:
    ENVIRONMENT = environment
    DATA_BASE_URI=os.getenv('DATA_BASE_URI')
    SECRET_KEY=os.getenv('SECRET_KEY')
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    APP_NAME=os.getenv('APP_NAME')