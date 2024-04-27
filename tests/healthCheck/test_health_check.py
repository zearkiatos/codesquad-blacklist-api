from unittest import TestCase, mock, main
from http import HTTPStatus
from  config import Config
from http import HTTPStatus
from flaskr.views.healthCheck.HealthCheckView import HealthCheckView

config = Config()

class TestHealthCheck(TestCase):
    @mock.patch.object(HealthCheckView, "get")
    def test_health_check(self, mock_get):
        expected =  {
                'environment': config.ENVIRONMENT,
                'application': config.APP_NAME,
                'status': HTTPStatus.OK
            }
        # Create an instance of HealthCheckView
        mock_get.return_value.json.return_value  = expected
        mock_get.return_value.status_code = HTTPStatus.OK
        health_check_view = HealthCheckView()
        response = health_check_view.get()
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), expected)

if __name__ == '__main__':
    main()