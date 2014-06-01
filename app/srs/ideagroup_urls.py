# urls_dt.py
# IdeaGroup urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from ideagroup_views   import IdeaGroupList, IdeaGroupDetail, IdeaGroupAdd, IdeaGroupEdit, IdeaGroupDelete


urlpatterns = patterns('',

    # IdeaGroup  (List, Detail, Add, Edit, Delete, Test)
    url(r'^$',                    TemplateView.as_view(template_name="ideagroup.html")),
    url(r'^/$',                   IdeaGroupList.as_view(), name='ideagroup_list'),
    url(r'^/(?P<pk>\d+)$',        IdeaGroupDetail.as_view(), name='ideagroup-detail'),
    url(r'^/add$',                IdeaGroupAdd.as_view(), name='ideagroup_add'),
    url(r'^/(?P<pk>\d+)/edit$',   IdeaGroupEdit.as_view(), name='ideagroup_update'),
    url(r'^/(?P<pk>\d+)/delete$', IdeaGroupDelete.as_view(), name='ideagroup_delete'),
    url(r'^/test$',               TemplateView.as_view(template_name="ideagroup_test.html")),


    # Catch all view
    url(r'^',                             TemplateView.as_view(template_name="index.html")),

)
