"""
Definition of urls for new.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.main, name='main'),
    url(r'^home$', app.views.home, name='home'),
    url(r'^maps$', app.views.maps, name='maps'),
    url(r'^qanda$', app.views.qanda, name='qanda'),
    url(r'^support1$', app.views.support1, name='support1'),
    url(r'^output$', app.views.output, name='output'),
    url(r'^outcome$', app.views.outcome, name='outcome'),
    url(r'^feedback_output$', app.views.feedback_output, name='feedback_output'),
    url(r'^feedback$', app.views.feedback, name='feedback'),
    url(r'^register$', app.views.UserFormView.as_view(), name='register'),
    #url(r'^add$', app.views.ratingCreate.as_view(), name='add'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
