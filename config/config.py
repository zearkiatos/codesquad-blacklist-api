import os
from dotenv import load_dotenv

environment = os.getenv('FLASK_ENV')

if environment == 'development':
    load_dotenv(dotenv_path='.env.dev')
else:
    load_dotenv(dotenv_path='.env')


class Config:
    ENVIRONMENT = environment
    DATA_BASE_URI=os.getenv('DATA_BASE_URI')
    SECRET_KEY=os.getenv('SECRET_KEY')
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    APP_NAME=os.getenv('APP_NAME')