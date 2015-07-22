from rest_framework.views import APIView
from django.shortcuts import redirect
from web_ide.github.models import LoginRequest
from web_ide.settings import GITHUB_CLIENT_ID


class LoginView(APIView):
    def get(self, request):
        login_request = LoginRequest(GITHUB_CLIENT_ID)
        return redirect(login_request)
