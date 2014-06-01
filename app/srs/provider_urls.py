# urls_dt.py
# Provider urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from provider_views   import ProviderList, ProviderDetail, ProviderAdd, ProviderEdit, ProviderDelete


urlpatterns = patterns(
    '',

    # Provider  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="provider.html")),
    
    # List
    url(r'^/$',                   ProviderList.as_view(), name='provider_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        ProviderDetail.as_view(), name='provider-detail'),

    # Add
    url(r'^/add$',                login_required(ProviderAdd.as_view(), login_url='/login'), name='provider_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(ProviderEdit.as_view(), login_url='/login'), name='provider_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(ProviderDelete.as_view(), login_url='/login'),
        name='provider_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="provider_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
