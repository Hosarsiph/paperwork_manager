# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='boss',
            field=models.CharField(max_length=32, null=True, verbose_name='Jefe Directo', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[(b'JU', b'Jefe de Unidad'), (b'DG', b'Director General'), (b'DA', b'Director de \xc3\x81rea'), (b'EVL', b'Evaluador')], max_length=32, blank=True, help_text='Papel o posisici\xf3n de la persona responsable', null=True, verbose_name='Nombre del puesto'),
        ),
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\xc1rea Administrativa', choices=[(b'DGGC', b'DGGC'), (b'DGGTA', b'DGGTA')]),
        ),
    ]
