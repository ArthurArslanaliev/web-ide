import urllib


class LoginRequest:
    url = 'https://github.com/login/oauth/authorize'

    def __init__(self, client_id):
        self.scopes = ['user:email', 'public_repo']
        self.client_id = client_id

    def get_absolute_url(self):
        args = {'client_id': self.client_id, 'scope': ','.join(self.scopes)}
        url = '{}?{}'.format(self.url, urllib.urlencode(args))
        return url
