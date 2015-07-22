import urllib


class LoginRequest:
    def __init__(self, github_url, client_id, scopes):
        self.github_url = github_url
        self.client_id = client_id
        self.scopes = scopes

    def get_absolute_url(self):
        args = {'client_id': self.client_id, 'scope': ','.join(self.scopes)}
        url = '{}?{}'.format(self.github_url, urllib.urlencode(args))
        return url
