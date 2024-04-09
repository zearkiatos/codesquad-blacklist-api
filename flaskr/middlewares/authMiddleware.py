from flask import  request
from http import HTTPStatus
from config.config import Config

config=Config()

def require_bearer_token(f):
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, HTTPStatus.UNAUTHORIZED
        try:

            if token != config.JWT_SECRET_KEY:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, HTTPStatus.UNAUTHORIZED
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

        return f(*args, **kwargs)
    return wrapper