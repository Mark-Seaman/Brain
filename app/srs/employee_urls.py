# urls_dt.py
# Employee urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from employee_views   import EmployeeList, EmployeeDetail, EmployeeAdd, EmployeeEdit, EmployeeDelete


urlpatterns = patterns(
    '',

    # Employee  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="employee.html")),
    
    # List
    url(r'^/$',                   EmployeeList.as_view(), name='employee_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        EmployeeDetail.as_view(), name='employee-detail'),

    # Add
    url(r'^/add$',                login_required(EmployeeAdd.as_view(), login_url='/login'), name='employee_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(EmployeeEdit.as_view(), login_url='/login'), name='employee_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(EmployeeDelete.as_view(), login_url='/login'),
        name='employee_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="employee_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
