from unittest import TestCase, mock, main
from  config import Config
from flask import Flask
import json
from flaskr.views.GlobalBlackList import GlobalBlackListView
from flaskr.middlewares import *


config = Config()
app = Flask(__name__)
class TestGlobalBlackList(TestCase):
    @mock.patch.object(GlobalBlackListView, "queryEmailInBlackList")
    def test_return_401_UNAUTHORIZED_if_token_is_not_sent(self,mock_query_email):
        email = "test@example.com"
        mock_query_email.return_value = {}
        global_black_list = GlobalBlackListView()

        @require_bearer_token
        def dummy_get_with_token():
            return global_black_list.get(email)

        with app.test_request_context(headers={}):
            response, status_code = dummy_get_with_token(email)

            self.assertEqual(status_code, 401)
            self.assertTrue(response['message'])
            self.assertEqual(response['message'], 'Authentication Token is missing!')
            self.assertEqual(response['error'], 'Unauthorized')

    def test_get_method_with_token_present(self):
        with mock.patch.object(GlobalBlackListView, "get") as mock_query_email:
            email = "test@example.com"
            espected= {
                    "exist": True,
                    "reason": "Este correo ha sido bloqueado debido a actividades sospechosas."
                }
            mock_query_email.return_value = espected
            
            @require_bearer_token
            def dummy_get_method(email):
                return espected, 200

            with app.test_request_context(headers={'Authorization': f'Bearer {config.JWT_SECRET_KEY}'}):
                response, status_code = dummy_get_method(email)

                self.assertEqual(status_code, 200)
                self.assertTrue(response['exist'])
                self.assertEqual(response['reason'], "Este correo ha sido bloqueado debido a actividades sospechosas.")

    def test_post_method_with_token_present(self):
        with mock.patch.object(GlobalBlackListView, "post") as mock_response:
            espected= {
                    "message": "Correo agregado a la lista negra correctamente"
                },
            data = {
                'email': 'test@example.com',
                'app_uuid':'8e97bdaa-7bc7-4fc4-92d4-1ea5f7bb8cbb',
                "blocked_reason": "Este correo ha sido bloqueado debido a actividades sospechosas."
            }
            mock_response.return_value = espected
            
            @require_bearer_token
            def dummy_post_method():
                return espected, 201

            with app.test_request_context(
                        headers={'Authorization': f'Bearer {config.JWT_SECRET_KEY}'},
                        data=json.dumps(data),
                    ):
                response, status_code = dummy_post_method()

                self.assertEqual(status_code, 201)
                self.assertTrue(response[0]['message'])


if __name__ == '__main__':
    main()