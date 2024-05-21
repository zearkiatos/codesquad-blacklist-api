from flask_restful import Resource
from http import HTTPStatus
from  config import Config
from ...utils.logger import Logger

log = Logger()

config = Config()

class HealthCheckView(Resource):
    def get(self):
        try:
            log.info('Receive healthcheck request')
            return {
                    'environment': config.ENVIRONMENT,
                    'application': config.APP_NAME,
                    'status': HTTPStatus.OK
                }, HTTPStatus.OK
        except Exception as ex:
            log.error('Something was wrong')
            return {
                'message': 'Something was wrong'
            }, HTTPStatus.INTERNAL_SERVER_ERROR