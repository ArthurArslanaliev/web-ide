import urlparse
import requests

from web_ide.github.settings import OAUTH_URL, API_URL


class GithubAPI:
    def __init__(self):
        pass

    @staticmethod
    def get_access_token(client_id, client_secret, code):
        url = '{}/{}'.format(OAUTH_URL, 'access_token')

        body = {
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code
        }

        headers = {'accept': 'application/json'}

        resp = requests.post(url, body, headers=headers)
        access_token = resp.json()['access_token']
        return access_token

    @staticmethod
    def get_user(access_token):
        resp = GithubAPIRequests.get('user', access_token)
        return resp.json()

    @staticmethod
    def get_user_public_repositories(access_token):
        resp = GithubAPIRequests.get('/user/repos?type=public', access_token)
        return resp.json()

    @staticmethod
    def get_user_public_repository(login, repository_name):
        resp = GithubAPIRequests.get('/repos/{login}/{repo_name}'.format(
            login=login,
            repo_name=repository_name
        ))
        return resp.json()


class GithubAPIRequests:
    def __init__(self):
        pass

    @staticmethod
    def get(resource, access_token=None):
        headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        if access_token:
            headers['Authorization'] = 'token {}'.format(access_token)

        resp = requests.get(urlparse.urljoin(API_URL, resource), headers=headers)
        return resp
