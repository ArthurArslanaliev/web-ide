from django.http.response import HttpResponseForbidden
from rest_framework.response import Response
from rest_framework.views import APIView

from web_ide.repository.repository import LocalRepositoryService
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
            # TODO: Add LocalRepository look-up here ???
            query = request.query_params
            path = query['path']
            base64_content = FileBrowser.get_content_base_64(path)
            return Response(data=base64_content)
        else:
            return HttpResponseForbidden()

    def put(self, request):
        access_token = take_access_token_from_session(request)
        if access_token:
            data = request.data
            path = data['path']
            content = data['content']
            FileBrowser.set_content(path, content)
            return Response()
        else:
            return HttpResponseForbidden()


class CreateEntityView(APIView):
    def post(self, request, local_repository_id):
        access_token = take_access_token_from_session(request)
        if access_token:
            data = request.data
            local_repository = LocalRepository.objects.get(id=local_repository_id)

            assert isinstance(local_repository, LocalRepository)

            file_browser = FileBrowser(local_repository.path)
            file_browser.create_new_entity(data['path'], data['type'])
            structure = file_browser.get_structure()

            return Response(data=structure)
        else:
            return HttpResponseForbidden()


class RenameEntityView(APIView):
    def put(self, request, local_repository_id):
        access_token = take_access_token_from_session(request)
        if access_token:
            data = request.data
            local_repository = LocalRepository.objects.get(id=local_repository_id)
            file_browser = FileBrowser(local_repository.path)
            file_browser.rename(data['source'], data['destination'])
            structure = file_browser.get_structure()

            return Response(data=structure)
        else:
            return HttpResponseForbidden()


class ExecuteCommandView(APIView):
    def post(self, request, local_repository_id):
        access_token = take_access_token_from_session(request)
        if access_token:
            command = request.data['command']
            local_repository = LocalRepository.objects.get(id=local_repository_id)
            result = LocalRepositoryService.execute_command(local_repository.path, command)
            return Response(data=result)
        else:
            return HttpResponseForbidden()
