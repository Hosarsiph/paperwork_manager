#encoding:utf-8

from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

from mia.models import Mia


class MiaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MiaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
          self.fields['situacion_actual'].widget.attrs['readonly'] = True
          self.fields['estatus'].widget.attrs['readonly'] = True

    class Meta:
        model = Mia

        widgets = {
            # Use localization and bootstrap 3
            'fecha_ingreso': DateWidget(attrs={'id':"id_fecha_ingreso"}, usel10n = True, bootstrap_version=3),
            'fecha_asigna_evaluador': DateWidget(attrs={'id':"id_fecha_asigna_evaluador"}, usel10n = True, bootstrap_version=3),
            'fecha_emisi_resolu': DateWidget(attrs={'id':"id_fecha_emisi_resolu"}, usel10n = True, bootstrap_version=3),
            'fecha_notifica_resolu': DateWidget(attrs={'id':"id_fecha_notifica_resolu"}, usel10n = True, bootstrap_version=3),
            'fecha_publica_extracto': DateWidget(attrs={'id':"id_fecha_publica_extracto"}, usel10n = True, bootstrap_version=3),
            'fecha_of_apercibimiento': DateWidget(attrs={'id':"id_fecha_of_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_notica_apercibimiento': DateWidget(attrs={'id':"id_fecha_notica_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_termi_apercibimiento': DateWidget(attrs={'id':"id_fecha_termi_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_entrega_apercibimiento': DateWidget(attrs={'id':"id_fecha_entrega_apercibimiento"}, usel10n = True, bootstrap_version=3),
            'fecha_of_infoadicional': DateWidget(attrs={'id':"id_fecha_of_infoadicional"}, usel10n = True, bootstrap_version=3),
            'fecha_notifi_of_infoadicional': DateWidget(attrs={'id':"id_fecha_notifi_of_infoadicional"}, usel10n = True, bootstrap_version=3),
            'fecha_vernci_of_infoadicional': DateWidget(attrs={'id':"id_fecha_vernci_of_infoadicional"}, usel10n = True, bootstrap_version=3),
            'fecha_entrega_of_infoadicional': DateWidget(attrs={'id':"id_fecha_entrega_of_infoadicional"}, usel10n = True, bootstrap_version=3),
        }
        exclude = ['id', 'user']
