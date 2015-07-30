import urlparse

import requests


class GithubRequests:
    def __init__(self, api_url, token):
        self.__api_url = api_url
        self.__token = token

    def get(self, resource):
        headers = {
            'Authorization': 'token {}'.format(self.__token),
            'Accept': 'application/vnd.github.v3+json'
        }

        resp = requests.get(urlparse.urljoin(self.__api_url, resource), headers=headers)
        return resp
