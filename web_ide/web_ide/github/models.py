import urllib
import requests
from web_ide.models import GithubUser

from web_ide.github.utils import GithubRequests


class AuthRequest:
    def __init__(self, url, client_id, scopes):
        self.__github_url = url
        self.__client_id = client_id
        self.__scopes = scopes

    def get_absolute_url(self):
        query = {'client_id': self.__client_id, 'scope': ','.join(self.__scopes)}
        url = '{}?{}'.format(self.__github_url, urllib.urlencode(query))
        return url


class AccessTokenRequest:
    def __init__(self, url, client_id, client_secret, code):
        self.__url = url
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__code = code

    def make(self):
        body = {'client_id': self.__client_id, 'client_secret': self.__client_secret, 'code': self.__code}
        headers = {'accept': 'application/json'}
        resp = requests.post(self.__url, body, headers=headers)
        access_token = resp.json()['access_token']
        return access_token


class GithubUserBuilder:
    def __init__(self, user_data):
        self._user_data = user_data

    def build(self):
        return GithubUser(id=self._user_data['id'],
                          login=self._user_data['login'])


class GithubRepository:
    def __init__(self, id, full_name, description, clone_url):
        self.id = id
        self.full_name = full_name
        self.description = description
        self.clone_url = clone_url

    @classmethod
    def build(cls, raw_repository):
        return cls(raw_repository['id'],
                   raw_repository['full_name'],
                   raw_repository['description'],
                   raw_repository['clone_url'])

    @staticmethod
    def serialize(instance):
        return vars(instance)


class GithubUserRequest:
    def __init__(self, api_url, token):
        self.__api_url = api_url
        self.__token = token

    def make(self):
        resp = GithubRequests(self.__api_url, self.__token).get('user')
        user_data = resp.json()
        return GithubUserBuilder(user_data).build()


class GithubUserRepositoriesRequest:
    def __init__(self, api_url, token):
        self.__api_url = api_url
        self.__token = token

    def make(self):
        req = GithubRequests(self.__api_url, self.__token)
        resp = req.get('/user/repos')
        repositories = resp.json()
        return map(GithubRepository.build, repositories)
