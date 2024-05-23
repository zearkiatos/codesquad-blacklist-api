from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .utils.json_custom_encoder import JSONCustomEncoder
from flaskr import create_app
from config import Config
from .views import HealthCheckView,GlobalBlackListView,ErrorsListView
from .dataContext.sqlAlchemyContext import db
import signal
import logging



config = Config()


application = create_app('default')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('default')

logger.info('Starting application....')

def before_server_stop(*args, **kwargs):
    logger.info('Closing application ...')


signal.signal(signal.SIGTERM, before_server_stop)


application.json_encoder = JSONCustomEncoder

cors = CORS(application)

if config.ENVIRONMENT != "test":
    app_context = application.app_context()
    app_context.push()
    #initialize database
    db.init_app(application)
    db.create_all()

api = Api(application)

#resources
api.add_resource(HealthCheckView, '/health')
api.add_resource(GlobalBlackListView, '/blacklists/<string:email>',endpoint='verify')
api.add_resource(GlobalBlackListView, '/blacklists',endpoint='create')
api.add_resource(ErrorsListView, '/GenerateError',endpoint='generate_error')



jwt = JWTManager(application)