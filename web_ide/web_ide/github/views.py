from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from web_ide.github.models import AuthRequest, AccessTokenRequest
from web_ide.github.keys import SECRET_KEY, CLIENT_ID
from web_ide.github.settings import AUTH_URL, SCOPES, ACCESS_TOKEN_URL


class AuthView(APIView):
    def get(self, request):
        auth_request = AuthRequest(AUTH_URL, CLIENT_ID, SCOPES)
        return redirect(auth_request)


class CallbackView(APIView):
    def get(self, request):
        if 'code' in request.query_params:
            access_token_request = AccessTokenRequest(ACCESS_TOKEN_URL, CLIENT_ID, SECRET_KEY,
                                                      request.query_params['code'])
            access_token = access_token_request.get_token()
            request.session['access_token'] = access_token
            return redirect('/')
        else:
            raise Exception()
