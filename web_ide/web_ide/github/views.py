from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from web_ide.github.models import AuthRequest, AccessTokenRequest, GithubUserRequest, GithubUserRepositoriesRequest, \
    GithubRepository
from web_ide.github.keys import SECRET_KEY, CLIENT_ID
from web_ide.github.settings import AUTH_URL, SCOPES, ACCESS_TOKEN_URL, API_URL


class AuthView(APIView):

    def get(self, request):

        auth_request = AuthRequest(AUTH_URL, CLIENT_ID, SCOPES)
        return redirect(auth_request)


class CallbackView(APIView):

    def get(self, request):

        if 'code' in request.query_params:
            access_token_request = AccessTokenRequest(ACCESS_TOKEN_URL, CLIENT_ID, SECRET_KEY,
                                                      request.query_params['code'])

            access_token = access_token_request.make()
            user = GithubUserRequest(API_URL, access_token).make()
            user.save()

            request.session['access_token'] = access_token
            request.session['user'] = user

            return redirect('/')
        else:
            raise Exception()


class LogoutView(APIView):

    def post(self, request):

        if request.session and 'user' in request.session:
            del request.session['user']

            return Response(data=None, status=204)


class RepositoriesView(APIView):

    def get(self, request):
        if request.session and 'user' in request.session and 'access_token' in request.session:
            access_token = request.session['access_token']
            repository_request = GithubUserRepositoriesRequest(API_URL, access_token)
            repositories = repository_request.make()
            return Response(data=map(GithubRepository.serialize, repositories))
        else:
            HttpResponseForbidden()