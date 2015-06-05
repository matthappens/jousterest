# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0002_auto_20150525_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date created'),
        ),
    ]
