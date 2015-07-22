from rest_framework.views import APIView

from django.shortcuts import render_to_response
from web_ide.settings import APP_URL


class Index(APIView):
    def get(self, request):
        params = {'APP_URL': APP_URL}
        return render_to_response('index.html', params)
