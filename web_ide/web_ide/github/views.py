from django.shortcuts import redirect
from rest_framework.views import APIView

from web_ide.github.models import LoginRequest
from web_ide.github.settings import AUTH_URL, CLIENT_ID, SCOPES


class LoginView(APIView):
    def get(self, request):
        login_request = LoginRequest(AUTH_URL, CLIENT_ID, SCOPES)
        return redirect(login_request)
