# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20161123_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\xc1rea Administrativa', choices=[(b'DGGC', b'DGGC'), (b'DGGTA', b'DGGTA'), (b'DGIE', b'DGIE'), (b'DGGPI', b'DGGPI')]),
        ),
    ]
