import mock

from django.test import TestCase
from tests.github.mocks.mocks import MockResponse

from web_ide.github.models import AccessTokenRequest


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
        actual_token = request.make()

        mock_requests.post.assert_called_once_with('url',
                                                   {'client_secret': client_secret, 'code': code,
                                                    'client_id': client_id},
                                                   headers={'accept': 'application/json'})

        self.assertEqual(actual_token, expected_token)
