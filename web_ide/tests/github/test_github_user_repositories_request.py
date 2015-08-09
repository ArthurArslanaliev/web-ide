import mock

from unittest import TestCase
from mock.mock import Mock
from tests.github.mocks.mocks import MockResponse
from web_ide.github.models import GithubUserRepositoriesRequest, GithubRepository


class GithubUserRepositoriesRequestTest(TestCase):
    @mock.patch('web_ide.github.models.GithubRequests')
    def test_make(self, github_requests_mock):
        api_url = 'https://github.com'
        token = 'access_token'
        expected_resource = '/user/repos'
        repo_id = 'repo1'
        repo_full_name = 'user/awesome'
        repo_description = 'my awesome repository'
        repo_clone_url = 'https://clone.git'

        instance_mock = Mock()
        instance_mock.get.return_value = MockResponse([{
            'id': repo_id,
            'full_name': repo_full_name,
            'description': repo_description,
            'clone_url': repo_clone_url
        }])

        github_requests_mock.return_value = instance_mock

        request = GithubUserRepositoriesRequest(api_url, token)
        repositories = request.make()
        repository_model = repositories[0]

        github_requests_mock.assert_called_once_with(api_url, token)
        instance_mock.get.assert_called_once_with(expected_resource)

        self.assertIsInstance(repository_model, GithubRepository)
        self.assertEqual(repository_model.id, repo_id)
        self.assertEqual(repository_model.full_name, repo_full_name)
        self.assertEqual(repository_model.description, repo_description)
        self.assertEqual(repository_model.clone_url, repo_clone_url)
