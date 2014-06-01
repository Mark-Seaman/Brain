# urls_dt.py
# Idea urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from idea_views   import IdeaList, IdeaDetail, IdeaAdd, IdeaEdit, IdeaDelete


urlpatterns = patterns(
    '',

    # Idea  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="idea.html")),
    
    # List
    url(r'^/$',                   IdeaList.as_view(), name='idea_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        IdeaDetail.as_view(), name='idea-detail'),

    # Add
    url(r'^/add$',                login_required(IdeaAdd.as_view(), login_url='/login'), name='idea_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(IdeaEdit.as_view(), login_url='/login'), name='idea_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(IdeaDelete.as_view(), login_url='/login'),
        name='idea_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="idea_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
