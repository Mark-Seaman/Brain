# urls_dt.py
# IdeaFeedback urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from ideafeedback_views   import IdeaFeedbackList, IdeaFeedbackDetail, IdeaFeedbackAdd, IdeaFeedbackEdit, IdeaFeedbackDelete


urlpatterns = patterns(
    '',

    # IdeaFeedback  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="ideafeedback.html")),
    
    # List
    url(r'^/$',                   IdeaFeedbackList.as_view(), name='ideafeedback_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        IdeaFeedbackDetail.as_view(), name='ideafeedback-detail'),

    # Add
    url(r'^/add$',                login_required(IdeaFeedbackAdd.as_view(), login_url='/login'), name='ideafeedback_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(IdeaFeedbackEdit.as_view(), login_url='/login'), name='ideafeedback_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(IdeaFeedbackDelete.as_view(), login_url='/login'),
        name='ideafeedback_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="ideafeedback_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
