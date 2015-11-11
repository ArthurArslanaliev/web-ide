from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from web_ide.repository.file_browser import FileBrowser
from web_ide.common.utils import take_access_token_from_session
from web_ide.repository.repository import LocalRepositoryService
from web_ide.models import GithubUser, LocalRepository
from web_ide.github.utils import take_keys, AuthRequest
from web_ide.github.builders import GithubUserBuilder, GithubRepositoryBuilder
from web_ide.github.api import GithubAPI
from web_ide.github.keys import SECRET_KEY, CLIENT_ID
from web_ide.github.settings import AUTH_URL, SCOPES


class AuthView(APIView):
    def get(self, request):
        auth_request = AuthRequest(AUTH_URL, CLIENT_ID, SCOPES)
        return redirect(auth_request)


class CallbackView(APIView):
    def get(self, request):

        if 'code' in request.query_params:
            code = request.query_params['code']
            access_token = GithubAPI.get_access_token(CLIENT_ID, SECRET_KEY, code)

            resp_data = GithubAPI.get_user(access_token)
            print(resp_data)

            user = GithubUserBuilder.build(resp_data)
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
            del request.session['access_token']

            return Response(data=None, status=204)


class RepositoriesView(APIView):
    def get(self, request):
        access_token = take_access_token_from_session(request)

        if access_token:
            resp_data = GithubAPI.get_user_public_repositories(access_token)
            serialize = lambda x: take_keys(x, ['id', 'name', 'full_name', 'clone_url', 'description'])
            return Response(data=map(serialize, resp_data))
        else:
            return HttpResponseForbidden()


class RepositoryView(APIView):
    def post(self, request, repository_name):
        access_token = take_access_token_from_session(request)
        if access_token:
            user = request.session['user']

            assert isinstance(user, GithubUser)

            resp_data = GithubAPI.get_user_public_repository(user.login, repository_name)
            github_repository = GithubRepositoryBuilder.build(resp_data, user)
            github_repository.save()

            # try to fetch repository by session_key and check if exists on file_system
            # before initializing the new one

            # also think of uniqueness of user_session

            session_key = request.session.session_key
            query_set = LocalRepository.objects.filter(user_session_key=session_key,
                                                       github_repository_id=github_repository.id) \
                .order_by('-last_modified')

            if query_set.exists():
                local_repo = query_set.first()
                if FileBrowser.repo_exists(local_repo.path):
                    return Response(data={'id': local_repo.id})

            local_repository = LocalRepositoryService.init_repository(session_key, github_repository)
            local_repository.save()

            return Response(data={'id': local_repository.id})
        else:
            return HttpResponseForbidden()
