import mock

from unittest import TestCase

from tests.github.mocks.mocks import MockResponse
from web_ide.github.api import GithubAPI, GithubAPIRequests


class GithubAPITest(TestCase):
    @mock.patch('web_ide.github.api.requests')
    @mock.patch('web_ide.github.api.OAUTH_URL', 'url')
    def test_get_access_token(self, mock_requests):
        client_id = 'client_id'
        client_secret = 'client_secret'
        code = 'code'
        expected_token = 'access_token'
        mock_requests.post.return_value = MockResponse({'access_token': expected_token})

        actual_token = GithubAPI.get_access_token(client_id, client_secret, code)

        mock_requests.post.assert_called_once_with('url/access_token', {
            'client_secret': client_secret,
            'code': code,
            'client_id': client_id
        }, headers={'accept': 'application/json'})

        self.assertEqual(actual_token, expected_token)

    @mock.patch('web_ide.github.api.GithubAPIRequests')
    def test_get_user(self, github_api_requests_mock):
        access_token = 'token'
        expected_user = 'test user'
        github_api_requests_mock.get.return_value = MockResponse(expected_user)

        user = GithubAPI.get_user(access_token)

        self.assertEqual(user, expected_user)
        github_api_requests_mock.get.assert_called_once_with('user', access_token)

    @mock.patch('web_ide.github.api.GithubAPIRequests')
    def test_get_user_public_repositories(self, github_api_requests_mock):
        access_token = 'token'
        expected_repositories = [{'id': 1}, {'id': 2}]
        github_api_requests_mock.get.return_value = MockResponse(expected_repositories)

        repositories = GithubAPI.get_user_public_repositories(access_token)

        self.assertEqual(repositories, expected_repositories)
        github_api_requests_mock.get.assert_called_once_with('/user/repos?type=public', access_token)


class GithubAPIRequestsTest(TestCase):
    @mock.patch('web_ide.github.api.requests')
    @mock.patch('web_ide.github.api.API_URL', 'http://github.com/')
    def test_get_with_token(self, mock_requests):
        resource = 'users'
        access_token = 'token'
        expected_resp = 'data'
        mock_requests.get.return_value = expected_resp

        data = GithubAPIRequests.get(resource, access_token)

        self.assertEqual(data, expected_resp)
        mock_requests.get.assert_called_once_with('http://github.com/%s' % resource, headers={
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token token'
        })

    @mock.patch('web_ide.github.api.requests')
    @mock.patch('web_ide.github.api.API_URL', 'http://github.com/')
    def test_get_without_token(self, mock_requests):
        resource = 'users'
        expected_resp = 'data'
        mock_requests.get.return_value = expected_resp

        data = GithubAPIRequests.get(resource, access_token=None)

        self.assertEqual(data, expected_resp)
        mock_requests.get.assert_called_once_with('http://github.com/%s' % resource, headers={
            'Accept': 'application/vnd.github.v3+json'
        })
