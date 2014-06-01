# app/urls.py
# Routes to views

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',  
    url(r'^$', 'srs.views.home', name='/'),
    url(r'^user$', 'srs.views.user', name='user'),
    url(r'^test$', 'srs.views.test_view', name='test'),
    url(r'^no_access$', 'srs.views.no_access'),

    url(r'^contact', include('srs.contact_urls')),

    (r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),  
    (r'^logout', 'srs.views.logout_view'),

)
