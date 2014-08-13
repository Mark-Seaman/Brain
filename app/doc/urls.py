from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join


admin.autodiscover()

urlpatterns = patterns(
    '',

    # Hammer views
    #url('login',                            'doc.views.login'),
    #url('logout',                           'doc.views.logout_view'),


    url(r'^$',                              'doc.views.home'),

    # url(r'^(?P<title>[\w\-_./]+)/new$',     'doc.views.new'),
    url(r'^(?P<title>[\w\-_./]+)/missing$', 'doc.views.missing'),
    # url(r'^(?P<title>[\w\-_./]+)/add$',     'doc.views.add'),
    # url(r'^(?P<title>[\w\-_./]+)/edit$',    'doc.views.edit'),
    # url(r'^(?P<title>[\w\-_./]+)/delete$',  'doc.views.delete'),

    url(r'^(?P<title>[\w\-_./]+)$',         'doc.views.doc'),

)
