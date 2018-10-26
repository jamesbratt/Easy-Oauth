
from django.conf.urls import url
from integration_config.views import (
    IntegrationListView,
    IntegrationCreate,
    IntegrationUpdate
)

app_name = 'integrations'
urlpatterns = [
    url(r'^create/$', IntegrationCreate.as_view(), name='create-integration'),
    url(r'^(?P<pk>[-\w]+)/$', IntegrationUpdate.as_view(), name='update-integration'),
    url(r'^$', IntegrationListView.as_view(), name='list-integrations'),
]