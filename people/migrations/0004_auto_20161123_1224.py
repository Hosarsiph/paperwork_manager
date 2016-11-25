# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20161122_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\xc1rea Administrativa', choices=[(b'DGGC', b'DGGC'), (b'DGGTA', b'DGGTA'), (b'DGIE', b'DGIE')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='boss',
            field=models.ForeignKey(related_name='user_boss', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Apellidos', blank=True),
        ),
    ]
