# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_ide', '0003_githubrepository_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalRepository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_session_key', models.CharField(unique=True, max_length=255)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('last_modified', models.DateTimeField()),
                ('github_repository', models.ForeignKey(to='web_ide.GithubRepository')),
            ],
        ),
    ]
