# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_ingreso', models.DateField(null=True, verbose_name='Fecha de Ingreso')),
                ('dias_evaluacion', models.IntegerField(default=0, null=True)),
                ('tramite_tiempo', models.CharField(default=b'SI', max_length=2, null=True, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('tipo_tramite', models.CharField(default=b'COFEMER', max_length=32, null=True, verbose_name='Tipo de tr\xe1mite', choices=[(b'COFEMER', b'COFEMER'), (b'IP', b'IP'), (b'MIA-P', b'MIA-P'), (b'MIA-P/ERA', b'MIA-P/ERA')])),
                ('bitacora', models.CharField(max_length=32, verbose_name='N\xfamero de bitacora')),
                ('numero_proyecto', models.CharField(max_length=32, null=True, verbose_name='N\xfamero de proyecto', blank=True)),
                ('estado_principal', models.CharField(max_length=64, null=True, verbose_name='Estado principal', blank=True)),
                ('estados', models.CharField(help_text='Estados que abarca el proyecto', max_length=64, null=True, verbose_name='Estados', blank=True)),
                ('municipio', models.CharField(help_text='Municipio que abarca el proyecto', max_length=128, null=True, verbose_name='Municipio', blank=True)),
                ('domicilio', models.CharField(max_length=254, null=True, verbose_name='Domicilio del Regulado', blank=True)),
                ('nombre_proyecto', models.CharField(max_length=512, null=True, verbose_name='Nombre del proyecto', blank=True)),
                ('regulado', models.CharField(max_length=254, null=True, verbose_name='Nombre del Regulado', blank=True)),
                ('representante_legal', models.CharField(max_length=254, null=True, verbose_name='Representante legal', blank=True)),
                ('subsector', models.CharField(max_length=32, null=True, verbose_name='Subsector', choices=[('PETR\xd3LEO', b'PETR\xc3\x93LEO'), ('PETROL\xcdFEROS', b'PETROL\xc3\x8dFEROS'), (b'GAS LP', b'GAS LP'), (b'GAS NATURAL', b'GAS NATURAL'), (b'RESIDUOS', b'RESIDUOS'), (b'DTU', b'DTU')])),
                ('tipo_instalacion', models.CharField(max_length=64, null=True, verbose_name='Tipo de instalaci\xf3n', choices=[('EXPLORACI\xd3N', b'EXPLORACI\xc3\x93N'), ('ESTACI\xd3N DE SERVICIO', b'ESTACI\xc3\x93N DE SERVICIO'), (b'ALMACENAMIENTO', b'ALMACENAMIENTO'), (b'TRANSPORTE', b'TRANSPORTE'), ('PLANTA DE DISTRIBUCI\xd3N', b'PLANTA DE DISTRIBUCI\xc3\x93N'), ('RED DE DISTRIBUCI\xd3N', b'RED DE DISTRIBUCI\xc3\x93N'), ('PROSPECCI\xd3N', b'PROSPECCI\xc3\x93N'), ('DESCOMPRENSI\xd3N DE GAS NATURAL', b'DESCOMPRENSI\xc3\x93N DE GAS NATURAL')])),
                ('ubicacion_instalacion', models.CharField(max_length=64, null=True, verbose_name='Ubicaci\xf3n de la instalaci\xf3n', choices=[(b'CARRETERA', b'CARRETERA'), (b'URBANA', b'URBANA'), (b'NA', b'NA'), (b'ZONA URBANA', b'ZONA URBANA')])),
                ('evaluador', models.CharField(max_length=64, null=True, verbose_name='Nombre del Evaluador')),
                ('fecha_asigna_evaluador', models.DateField(null=True, verbose_name='Fecha de asignaci\xf3n al Evaluador')),
                ('situacion_actual', models.CharField(max_length=128, null=True, verbose_name='Situaci\xf3n actual', blank=True)),
                ('estatus', models.CharField(blank=True, max_length=254, null=True, verbose_name='Estatus del proyecto', choices=[(b'RESUELTO', b'RESUELTO'), ('EN TR\xc1MITE', b'EN TR\xc3\x81MITE')])),
                ('numero_resolucion', models.CharField(max_length=128, null=True, verbose_name='N\xfamero de resoluci\xf3n', blank=True)),
                ('unidad_firma', models.CharField(max_length=16, null=True, verbose_name='Unidad que firma', blank=True)),
                ('fecha_emisi_resolu', models.DateField(null=True, verbose_name='Fecha de emisi\xf3n de resoluci\xf3n')),
                ('fecha_notifica_resolu', models.DateField(null=True, verbose_name='Fecha notificaci\xf3n de resoluci\xf3n')),
                ('sentido_resolucion', models.CharField(max_length=64, null=True, verbose_name='Setido resoluci\xf3n', blank=True)),
                ('vigencia_resolucion', models.CharField(max_length=16, null=True, verbose_name='Vigencia de resoluci\xf3n', blank=True)),
                ('fecha_publica_extracto', models.DateField(null=True, verbose_name='Fecha de publicaci\xf3n de extracto')),
                ('nume_of_apercibimiento', models.CharField(max_length=64, null=True, verbose_name='N\xfamero de oficio apercibimiento', blank=True)),
                ('fecha_of_apercibimiento', models.DateField(null=True, verbose_name='Fecha de oficio de apercibimiento', blank=True)),
                ('fecha_notica_apercibimiento', models.DateField(null=True, verbose_name='Fecha de notificaci\xf3n de apercibimiento')),
                ('fecha_termi_apercibimiento', models.DateField(null=True, verbose_name='Fecha de vencimiento de apercibimiento')),
                ('fecha_entrega_apercibimiento', models.DateField(null=True, verbose_name='Fecha de entrega de apercibimiento')),
                ('dias_transcurre_apercibimiento', models.CharField(max_length=32, null=True, verbose_name='D\xedas transcurridos de apercibimiento', blank=True)),
                ('numero_of_infoadicional', models.CharField(max_length=32, null=True, verbose_name='N\xfamero de informaci\xf3n adicional', blank=True)),
                ('fecha_of_infoadicional', models.DateField(null=True, verbose_name='Fecha de informaci\xf3n adicional')),
                ('fecha_notifi_of_infoadicional', models.DateField(null=True, verbose_name='Fecha de informaci\xf3n adicional')),
                ('fecha_vernci_of_infoadicional', models.DateField(null=True, verbose_name='Fecha de vencimiento de informaci\xf3n adicional')),
                ('fecha_entrega_of_infoadicional', models.DateField(null=True, verbose_name='Fecha de entrega de informaci\xf3n adicional')),
                ('dias_transcurre_of_infoadicional', models.IntegerField(default=0, null=True, verbose_name='D\xedas trasncurridos de informaci\xf3n adicional')),
                ('observasiones', models.CharField(max_length=512, null=True, verbose_name='Observaciones', blank=True)),
                ('numero_of_aplia_plazo', models.CharField(max_length=32, null=True, verbose_name='N\xfamero de plazo', blank=True)),
                ('dias_emision_resolucion', models.IntegerField(default=0, null=True, verbose_name='D\xedas emisi\xf3n de resoluci\xf3n')),
                ('resolucion_tiempo', models.CharField(default=b'SI', max_length=2, null=True, verbose_name='\xbfResoluci\xf3n en tiempo?', choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('dia_actual', models.DateField(auto_now=True, verbose_name='D\xeda actual')),
                ('lati', models.FloatField(null=True, verbose_name='Latitud', blank=True)),
                ('longi', models.FloatField(null=True, verbose_name='Longitud', blank=True)),
                ('dias_feriado', models.DateField(null=True, verbose_name='D\xedas feriados')),
                ('dias_habiles', models.DateField(null=True, verbose_name='D\xedas habiles')),
                ('estatus_proyect', models.CharField(max_length=32, null=True, verbose_name='Estatus del proyecto', choices=[(b'CONSTRUIDA', b'CONSTRUIDA'), ('EN CONSTRUCCI\xd3N', b'EN CONSTRUCCI\xc3\x93N'), ('OPERACI\xd3N', b'OPERACI\xc3\x93N'), (b'NUEVA', b'NUEVA'), (b'INICIO DE PROCEDIMIENTO', b'INICIO DE PROCEDIMIENTO')])),
                ('llave_pago', models.CharField(max_length=32, null=True, verbose_name='Llave de pago', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
