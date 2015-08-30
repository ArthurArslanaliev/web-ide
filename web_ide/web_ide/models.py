from django.db import models


class GithubUser(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    login = models.CharField(max_length=256)

