# urls_dt.py
# Driver urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from driver_views   import DriverList, DriverDetail, DriverAdd, DriverEdit, DriverDelete


urlpatterns = patterns(
    '',

    # Driver  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="driver.html")),
    
    # List
    url(r'^/$',                   DriverList.as_view(), name='driver_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        DriverDetail.as_view(), name='driver-detail'),

    # Add
    url(r'^/add$',                login_required(DriverAdd.as_view(), login_url='/login'), name='driver_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(DriverEdit.as_view(), login_url='/login'), name='driver_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(DriverDelete.as_view(), login_url='/login'),
        name='driver_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="driver_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
