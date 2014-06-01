# urls_dt.py
# Award urls

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from award_views   import AwardList, AwardDetail, AwardAdd, AwardEdit, AwardDelete


urlpatterns = patterns(
    '',

    # Award  (List, Detail, Add, Edit, Delete, Test)

    #Home
    url(r'^$',                    TemplateView.as_view(template_name="award.html")),
    
    # List
    url(r'^/$',                   AwardList.as_view(), name='award_list'),
    
    # Detail
    url(r'^/(?P<pk>\d+)$',        AwardDetail.as_view(), name='award-detail'),

    # Add
    url(r'^/add$',                login_required(AwardAdd.as_view(), login_url='/login'), name='award_add'),

    # Edit
    url(r'^/(?P<pk>\d+)/edit$',   login_required(AwardEdit.as_view(), login_url='/login'), name='award_update'),

    # Delete
    url(r'^/(?P<pk>\d+)/delete$', login_required(AwardDelete.as_view(), login_url='/login'),
        name='award_delete'),

    # Test
    url(r'^/test$',               login_required(TemplateView.as_view(template_name="award_test.html"), login_url='/login')),

    # Catch all view
    url(r'^',                     TemplateView.as_view(template_name="missing.html")),

)
