import urllib

import requests


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
        headers = {'Accept': 'application/json'}
        resp = requests.post(self.__url, body, headers=headers)
        access_token = resp.json()['access_token']
        return access_token

