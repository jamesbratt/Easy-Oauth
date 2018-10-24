
from django.conf.urls import url
from project.views import (
    ProjectListView,
    ProjectCreate,
    ProjectUpdate,
    OauthLoginRedirect,
    GetOauthToken
)

app_name = 'project'
urlpatterns = [
    url(r'^create/$', ProjectCreate.as_view(), name='create-project'),
    url(r'^(?P<pk>[-\w]+)/$', ProjectUpdate.as_view(), name='update-project'),
    url(r'^login/(?P<pk>[-\w]+)/$', OauthLoginRedirect.as_view(), name='oauth-login'),
    url(r'^authorise/(?P<pk>[-\w]+)/$', GetOauthToken.as_view(), name='oauth-authorise'),
    url(r'^$', ProjectListView.as_view(), name='list-projects'),
]