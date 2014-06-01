# urls_dt.py
# Company urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from company_views   import CompanyList, CompanyDetail, CompanyAdd, CompanyEdit, CompanyDelete


urlpatterns = patterns(
    '',

    # Company  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="company.html")),
    
    # List
    url(r'^/$',                   CompanyList.as_view(), name='company_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        CompanyDetail.as_view(), name='company-detail'),

    # Add
    url(r'^/add$',                login_required(CompanyAdd.as_view(), login_url='/login'), name='company_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(CompanyEdit.as_view(), login_url='/login'), name='company_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(CompanyDelete.as_view(), login_url='/login'),
        name='company_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="company_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
