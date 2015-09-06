# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_ide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubRepository',
            fields=[
                ('id', models.BigIntegerField(unique=True, serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=255)),
                ('clone_url', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('github_user', models.ForeignKey(to='web_ide.GithubUser')),
            ],
        ),
    ]
