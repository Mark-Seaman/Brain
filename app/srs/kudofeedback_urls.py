# urls_dt.py
# KudoFeedback urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from kudofeedback_views   import KudoFeedbackList, KudoFeedbackDetail, KudoFeedbackAdd, KudoFeedbackEdit, KudoFeedbackDelete


urlpatterns = patterns(
    '',

    # KudoFeedback  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="kudofeedback.html")),
    
    # List
    url(r'^/$',                   KudoFeedbackList.as_view(), name='kudofeedback_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        KudoFeedbackDetail.as_view(), name='kudofeedback-detail'),

    # Add
    url(r'^/add$',                login_required(KudoFeedbackAdd.as_view(), login_url='/login'), name='kudofeedback_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(KudoFeedbackEdit.as_view(), login_url='/login'), name='kudofeedback_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(KudoFeedbackDelete.as_view(), login_url='/login'),
        name='kudofeedback_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="kudofeedback_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
