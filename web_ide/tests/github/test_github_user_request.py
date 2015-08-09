import mock

from unittest import TestCase
from mock.mock import Mock
from tests.github.mocks.mocks import MockResponse
from web_ide.github.models import GithubUserRequest, GithubUser


class GithubUserRequestTest(TestCase):

    @mock.patch('web_ide.github.models.GithubRequests')
    def test_get(self, github_requests_mock):
        api_url = 'https://github.com/'
        token = 'token'
        expected_login = 'login'
        expected_id = 'id'
        get_method_mock = Mock()
        get_method_mock.get.return_value = MockResponse({'id': expected_id, 'login': expected_login})
        github_requests_mock.return_value = get_method_mock

        github_user_request = GithubUserRequest(api_url, token)
        github_user = github_user_request.make()

        github_requests_mock.assert_called_once_with(api_url, token)
        get_method_mock.get.assert_called_once_with('user')
        self.assertIsInstance(github_user, GithubUser)
        self.assertEqual(github_user.id, expected_id)
        self.assertEqual(github_user.login, expected_login)