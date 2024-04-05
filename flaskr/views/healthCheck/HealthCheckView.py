from flask_restful import Resource
from http import HTTPStatus
from  config import Config

config = Config()

class HealthCheckView(Resource):
    def get(self):
        return {
                'environment': config.ENVIRONMENT,
                'application': config.APP_NAME,
                'status': HTTPStatus.OK
            }, HTTPStatus.OK