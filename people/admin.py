from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from people.models import user

# Register your models here.
class PeopleUserAdmin(UserAdmin):
    """docstring for PeopleUserAdmin."""

    fieldsets = ()
    add_fieldsets = (
        (None,{
            'fields': ('user', 'password1', 'password2'),
        }),
    )
    list_display = ('user', 'is_active', 'is_staff',)
    search_fields = ('user',)
    ordering = ('user',)

admin.site.register(user, PeopleUserAdmin)
