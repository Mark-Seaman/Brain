# urls_dt.py
# Group urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from group_views   import GroupList, GroupDetail, GroupAdd, GroupEdit, GroupDelete


urlpatterns = patterns(
    '',

    # Group  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="group.html")),
    
    # List
    url(r'^/$',                   GroupList.as_view(), name='group_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        GroupDetail.as_view(), name='group-detail'),

    # Add
    url(r'^/add$',                login_required(GroupAdd.as_view(), login_url='/login'), name='group_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(GroupEdit.as_view(), login_url='/login'), name='group_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(GroupDelete.as_view(), login_url='/login'),
        name='group_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="group_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
