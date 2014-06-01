# urls_dt.py
# KudoGroup urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from kudogroup_views   import KudoGroupList, KudoGroupDetail, KudoGroupAdd, KudoGroupEdit, KudoGroupDelete


urlpatterns = patterns('',

    # KudoGroup  (List, Detail, Add, Edit, Delete, Test)
    url(r'^$',                    TemplateView.as_view(template_name="kudogroup.html")),
    url(r'^/$',                   KudoGroupList.as_view(), name='kudogroup_list'),
    url(r'^/(?P<pk>\d+)$',        KudoGroupDetail.as_view(), name='kudogroup-detail'),
    url(r'^/add$',                KudoGroupAdd.as_view(), name='kudogroup_add'),
    url(r'^/(?P<pk>\d+)/edit$',   KudoGroupEdit.as_view(), name='kudogroup_update'),
    url(r'^/(?P<pk>\d+)/delete$', KudoGroupDelete.as_view(), name='kudogroup_delete'),
    url(r'^/test$',               TemplateView.as_view(template_name="kudogroup_test.html")),


    # Catch all view
    url(r'^',                             TemplateView.as_view(template_name="index.html")),

)
