import urllib


class AuthRequest:
    def __init__(self, url, client_id, scopes):
        self.__github_url = url
        self.__client_id = client_id
        self.__scopes = scopes

    def get_absolute_url(self):
        query = {'client_id': self.__client_id, 'scope': ','.join(self.__scopes)}
        url = '{}?{}'.format(self.__github_url, urllib.urlencode(query))
        return url


def take_keys(data, keys):
    return {key: data.get(key) for key in keys}
