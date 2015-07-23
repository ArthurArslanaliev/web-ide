BASE_URL = 'https://github.com/login/oauth'

AUTH_URL = '{}/{}'.format(BASE_URL, 'authorize')
ACCESS_TOKEN_URL = '{}/{}'.format(BASE_URL, 'access_token')

SCOPES = ['user:email', 'public_repo']


