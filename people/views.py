# -*- coding: utf-8 -*-

import json
import ast
import datetime
from datetime import date
import math

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.db.models import Avg

from django.db.models import CharField, Value as V
from django.db.models.functions import Concat

from itertools import groupby

from mia.models import Mia
from mia.models import user


def login_people(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/profile_detail')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/profile_detail')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('people/nouser.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('people/login_people.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/login_people')
def profile_detail(request):

    detail_evalu = {}
    usuario = request.user
    first_name =  user.objects.values_list('first_name', flat=True).filter(Q(boss=usuario))
    last_name = user.objects.values_list('last_name', flat=True).filter(Q(boss=usuario))
    if usuario.position == 'DA':
        for f, l in zip(first_name, last_name):
            evaluadores = f + l
            mia = Mia.objects.filter(evaluador=evaluadores)
            detail_evalu[evaluadores] = mia
    else:
        evaluador =  usuario.first_name + usuario.last_name
        detail_evalu[evaluador] = Mia.objects.filter(evaluador=evaluador)

    return render_to_response('people/profile_detail.html', {
                                                            'usuario': usuario,
                                                            'evalua_to_dic': detail_evalu,
                                                            }, context_instance=RequestContext(request))

@login_required(login_url='/login_people')
def logout_people(request):
    logout(request)
    return HttpResponseRedirect('/')
