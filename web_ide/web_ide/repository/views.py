from django.http.response import HttpResponseForbidden
from rest_framework.response import Response
from rest_framework.views import APIView

from web_ide.repository.file_browser import FileBrowser
from web_ide.models import LocalRepository
from web_ide.common.utils import take_access_token_from_session


class StructureView(APIView):
    def get(self, request, local_repository_id):
        access_token = take_access_token_from_session(request)
        if access_token:
            local_repository = LocalRepository.objects.get(id=local_repository_id)

            assert isinstance(local_repository, LocalRepository)

            file_browser = FileBrowser(local_repository.path)
            structure = file_browser.get_structure()

            return Response(data=structure)
        else:
            return HttpResponseForbidden()


class ContentView(APIView):
    def get(self, request):
        access_token = take_access_token_from_session(request)
        if access_token:
            query = request.query_params
            path = query['path']
            base64_content = FileBrowser.get_content_base_64(path)
            return Response(data=base64_content)
        else:
            return HttpResponseForbidden()
