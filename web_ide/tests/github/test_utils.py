import mock

from unittest import TestCase
from requests import Response

from web_ide.github.utils import GithubRequests


class GithubRequestsTest(TestCase):

    @mock.patch('web_ide.github.utils.requests')
    def test_get(self, mock_requests):
        api_url = 'https://github.com'
        token = 'token'
        resource = 'users'
        mock_requests.get.return_value = Response()

        request = GithubRequests(api_url, token)
        resp = request.get(resource)

        mock_requests.get.assert_called_once_with('https://github.com/users',
                                                  headers={'Accept': 'application/vnd.github.v3+json',
                                                           'Authorization': 'token token'})
        self.assertIsInstance(resp, Response)
