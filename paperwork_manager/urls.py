
# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin


# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'ugi.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# ]
js_info_dict = {
    'domain': 'djangojs',
    'packages': ('paperwork_manager',)
}

urlpatterns = patterns('',

                        # Static pages
                        # url(r'^/?$', TemplateView.as_view(template_name='index.html'), name='home'),
                        url(r'^$', 'people.views.login_people', name='login_people'),
                        url(r'^admin/', include(admin.site.urls)),

                         # Mia views
                         (r'^', include('mia.urls')),

                         # People views
                         (r'^', include('people.urls')),
                         # url(r'^profile_detail/$','ugi.people.views.profile_detail'),


                        )
