# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# area = models.CharField(
#         _('Administrative Area'),
#         max_length=255,
#         blank=True,
#         null=True,
#         help_text=_('state, province of the location'))

lbl_area = (
    ('DGGC', 'DGGC'),
    ('DGGTA', 'DGGTA'),
    ('DGIE', 'DGIE'),
    ('DGGPI', 'DGGPI'),
)
lbl_position = (
    ('JU', 'Jefe de Unidad'),
    ('DG', 'Director General'),
    ('DA', 'Director de Área'),
    ('EVL', 'Evaluador'),
)

class PeopleBaseUserManager(BaseUserManager):
    """docstring for PeopleBaseUserManager."""

    def create_user(self, user, password):
        user = self.model(user=user)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user, password):
        user = self.create_user(user, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class user(AbstractBaseUser, PermissionsMixin):
    """docstring for user."""

    user = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(_('Nombre'), max_length=30, blank=True)
    last_name = models.CharField(_('Apellidos'), max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    area = models.CharField(
        _(u'Área Administrativa'),
        choices=lbl_area,
        blank=True,
        null=True,
        max_length=32)
    position = models.CharField(
        _('Nombre del puesto'),
        choices=lbl_position,
        blank=True,
        null=True,
        max_length=32,
        help_text=_(u'Papel o posisición de la persona responsable'))

    # boss = models.CharField(
    #     _('Jefe Directo'),
    #     blank=True,
    #     null=True,
    #     max_length=32)

    boss = models.ForeignKey("self", null=True, blank=True, related_name="user_boss")

    USERNAME_FIELD = 'user'

    objects = PeopleBaseUserManager()

    def get_full_name(self):
        return self.user

    def get_short_name(self):
        return self.user
