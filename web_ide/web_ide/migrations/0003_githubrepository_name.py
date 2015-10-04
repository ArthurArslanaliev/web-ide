# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_ide', '0002_githubrepository'),
    ]

    operations = [
        migrations.AddField(
            model_name='githubrepository',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
