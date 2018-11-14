from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from braces import views
from integration_config.models import IntegrationConf

class IntegrationCreate(views.LoginRequiredMixin,
                        views.SuperuserRequiredMixin,
                        CreateView):
    """ Creating a new integration """

    raise_exception = True
    model = IntegrationConf
    fields = ['title', 'module_path', 'oauth_class_name', 'form_class_name']

class IntegrationUpdate(views.LoginRequiredMixin,
                        views.SuperuserRequiredMixin,
                        UpdateView):
    """ Updating an existing integration """

    raise_exception = True
    model = IntegrationConf
    fields = ['title', 'module_path', 'oauth_class_name', 'form_class_name']
    template_name_suffix = '_update_form'

class IntegrationListView(views.LoginRequiredMixin,
                          views.SuperuserRequiredMixin,
                          ListView):
    """ Listing all integrations """

    raise_exception = True
    model = IntegrationConf
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """ Returning context """
        context = super().get_context_data(**kwargs)
        return context
