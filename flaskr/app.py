from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .utils.json_custom_encoder import JSONCustomEncoder
from flaskr import create_app
from config import Config
from .views import HealthCheckView
config = Config()


app = create_app('default')
app.json_encoder = JSONCustomEncoder

app_context = app.app_context()
app_context.push()

cors = CORS(app)

api = Api(app)

#resources
api.add_resource(HealthCheckView, '/health')

jwt = JWTManager(app)