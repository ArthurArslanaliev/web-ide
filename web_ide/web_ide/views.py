from rest_framework.views import APIView
from django.shortcuts import render_to_response

from web_ide.models import GithubUser
from web_ide.settings import APP_URL


class Index(APIView):
    def get(self, request):
        params = {'APP_URL': APP_URL}

        if request.session and 'user' in request.session:
            user = request.session['user']

            assert isinstance(user, GithubUser)

            params.update({
                'USER_LOGIN': user.login,
                'USER_ID': user.id,
                'USER_AVATAR_URL': user.avatar_url,
                'USER_ACCOUNT_URL': user.html_url
            })

            print(request.session['access_token'])

        return render_to_response('index.html', params)
