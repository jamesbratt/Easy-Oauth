from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from integration_config.models import IntegrationConf

class IntegrationCreate(CreateView):
    """ Creating a new integration """

    model = IntegrationConf
    fields = ['title', 'module_path', 'oauth_class_name', 'form_class_name']

class IntegrationUpdate(UpdateView):
    """ Updating an existing integration """

    model = IntegrationConf
    fields = ['title', 'module_path', 'oauth_class_name', 'form_class_name']
    template_name_suffix = '_update_form'

class IntegrationListView(ListView):
    """ Listing all integrations """

    model = IntegrationConf
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """ Returning context """
        context = super().get_context_data(**kwargs)
        return context
