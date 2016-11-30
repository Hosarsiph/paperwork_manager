# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mia',
            name='estatus_proyect',
            field=models.CharField(default=b'COFEMER', max_length=32, null=True, verbose_name='Estatus del proyecto', choices=[(b'CONSTRUIDA', b'CONSTRUIDA'), ('EN CONSTRUCCI\xd3N', b'EN CONSTRUCCI\xc3\x93N'), ('OPERACI\xd3N', b'OPERACI\xc3\x93N'), (b'NUEVA', b'NUEVA'), (b'INICIO DE PROCEDIMIENTO', b'INICIO DE PROCEDIMIENTO')]),
        ),
        migrations.AlterField(
            model_name='mia',
            name='fecha_notifi_of_infoadicional',
            field=models.DateField(null=True, verbose_name='Fecha de notificaci\xf3n informaci\xf3n adicional'),
        ),
    ]
