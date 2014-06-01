# urls_dt.py
# Behavior urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from behavior_views   import BehaviorList, BehaviorDetail, BehaviorAdd, BehaviorEdit, BehaviorDelete


urlpatterns = patterns(
    '',

    # Behavior  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="behavior.html")),
    
    # List
    url(r'^/$',                   BehaviorList.as_view(), name='behavior_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        BehaviorDetail.as_view(), name='behavior-detail'),

    # Add
    url(r'^/add$',                login_required(BehaviorAdd.as_view(), login_url='/login'), name='behavior_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(BehaviorEdit.as_view(), login_url='/login'), name='behavior_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(BehaviorDelete.as_view(), login_url='/login'),
        name='behavior_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="behavior_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
