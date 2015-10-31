from django.db import models


class GithubUser(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    login = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255, null=True)
    html_url = models.CharField(max_length=255, null=True)


class GithubRepository(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    clone_url = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    github_user = models.ForeignKey(GithubUser)


class LocalRepository(models.Model):
    user_session_key = models.CharField(max_length=255)
    path = models.CharField(max_length=255, unique=True)
    last_modified = models.DateTimeField(null=False)
    github_repository = models.ForeignKey(GithubRepository)
