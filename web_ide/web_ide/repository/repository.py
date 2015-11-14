import tempfile
import git

from git import Repo
from django.utils import timezone

from web_ide.models import GithubRepository, LocalRepository


class LocalRepositoryService(object):
    @staticmethod
    def init_repository(user_session_key, github_repository):
        assert isinstance(github_repository, GithubRepository)

        temp_dir = tempfile.mkdtemp()

        Repo.clone_from(github_repository.clone_url, temp_dir)

        return LocalRepository(path=temp_dir,
                               user_session_key=user_session_key,
                               last_modified=timezone.now(),
                               github_repository=github_repository)

    @staticmethod
    def execute_command(local_repository_path, command):
        g = git.Git(local_repository_path)
        try:
            return g.execute(command.split(' '))
        except git.exc.GitCommandNotFound as e:
            return "Error running: {}. Error: {}".format(command, e)
