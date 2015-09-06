from web_ide.models import GithubUser, GithubRepository


class GithubUserBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build(data):
        return GithubUser(id=data['id'],
                          login=data['login'],
                          avatar_url=data['avatar_url'],
                          html_url=data['html_url'])


class GithubRepositoryBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build(data, github_user):
        return GithubRepository(id=data['id'],
                                full_name=data['full_name'],
                                clone_url=data['clone_url'],
                                description=data['description'],
                                github_user=github_user)
