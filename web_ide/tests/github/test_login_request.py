import urllib

from django.test import TestCase

from web_ide.github.models import LoginRequest


class LoginRequestTest(TestCase):
    def test_get_absolute_url(self):
        client_id = 'client_id'
        github_url = 'https://github.com/login/oauth/authorize'
        scope = 'user'
        expected_url = '{}?scope={}&client_id={}'.format(github_url, scope, client_id)

        request = LoginRequest(github_url, client_id, [scope])
        actual_url = request.get_absolute_url()

        self.assertEqual(urllib.unquote(actual_url), expected_url)
