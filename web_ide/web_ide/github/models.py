import urllib

import requests
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

    def get_token(self):
        body = {'client_id': self.__client_id, 'client_secret': self.__client_secret, 'code': self.__code}
        headers = {'accept': 'application/json'}
        resp = requests.post(self.__url, body, headers=headers)
        access_token = resp.json()['access_token']
        return access_token


class GithubUser:
    def __init__(self, login, id):
        self.login = login
        self.id = id


class GithubUserRequest:
    def __init__(self, api_url, token):
        self.__api_url = api_url
        self.__token = token

    def get(self):
        resp = GithubRequests(self.__api_url, self.__token).get('user')
        user_data = resp.json()

        return GithubUser(user_data['id'], user_data['login'])
