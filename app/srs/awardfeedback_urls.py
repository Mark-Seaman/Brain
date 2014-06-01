# urls_dt.py
# AwardFeedback urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from awardfeedback_views   import AwardFeedbackList, AwardFeedbackDetail, AwardFeedbackAdd, AwardFeedbackEdit, AwardFeedbackDelete


urlpatterns = patterns(
    '',

    # AwardFeedback  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="awardfeedback.html")),
    
    # List
    url(r'^/$',                   AwardFeedbackList.as_view(), name='awardfeedback_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        AwardFeedbackDetail.as_view(), name='awardfeedback-detail'),

    # Add
    url(r'^/add$',                login_required(AwardFeedbackAdd.as_view(), login_url='/login'), name='awardfeedback_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(AwardFeedbackEdit.as_view(), login_url='/login'), name='awardfeedback_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(AwardFeedbackDelete.as_view(), login_url='/login'),
        name='awardfeedback_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="awardfeedback_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
