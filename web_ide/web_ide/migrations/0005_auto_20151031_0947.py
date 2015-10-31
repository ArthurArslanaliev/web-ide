# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_ide', '0004_localrepository'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localrepository',
            name='user_session_key',
            field=models.CharField(max_length=255),
        ),
    ]
