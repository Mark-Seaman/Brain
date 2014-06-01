# urls_dt.py
# Kudo urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from kudo_views   import KudoList, KudoDetail, KudoAdd, KudoEdit, KudoDelete


urlpatterns = patterns(
    '',

    # Kudo  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="kudo.html")),
    
    # List
    url(r'^/$',                   KudoList.as_view(), name='kudo_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        KudoDetail.as_view(), name='kudo-detail'),

    # Add
    url(r'^/add$',                login_required(KudoAdd.as_view(), login_url='/login'), name='kudo_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(KudoEdit.as_view(), login_url='/login'), name='kudo_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(KudoDelete.as_view(), login_url='/login'),
        name='kudo_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="kudo_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
