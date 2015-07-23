import mock

from django.test import TestCase

from web_ide.github.models import AccessTokenRequest


class MockResponse:
    def __init__(self, resp):
        self.__response = resp

    def json(self):
        return self.__response


class AuthRequestTest(TestCase):
    @mock.patch('web_ide.github.models.requests')
    def test_get_token(self, mock_requests):
        url = 'url'
        client_id = 'client_id'
        client_secret = 'client_secret'
        code = 'code'
        expected_token = 'access_token'
        mock_requests.post.return_value = MockResponse({'access_token': expected_token})

        request = AccessTokenRequest(url, client_id, client_secret, code)
        actual_token = request.get_token()

        mock_requests.post.assert_called_with('url',
                                              {'client_secret': client_secret, 'code': code, 'client_id': client_id},
                                              headers={'accept': 'application/json'})

        self.assertEqual(actual_token, expected_token)
