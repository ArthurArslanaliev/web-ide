# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubUser',
            fields=[
                ('id', models.BigIntegerField(unique=True, serialize=False, primary_key=True)),
                ('login', models.CharField(max_length=255)),
                ('avatar_url', models.CharField(max_length=255, null=True)),
                ('html_url', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
