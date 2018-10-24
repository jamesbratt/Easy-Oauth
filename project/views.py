from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from project.models import Project
from integrations.registry import getIntegrationFromRegistry


class OauthLoginRedirect(View):
    """ Redirect to an integrations authorization page """

    def get(self, request, **kwargs):
        """ Get the redirect url """
        fields = Project.objects.get(pk=self.kwargs['pk'])
        integration = getIntegrationFromRegistry(fields.app)
        integration_instance = integration(fields)
        url = integration_instance.get_auth_url()

        return HttpResponseRedirect(url)

class GetOauthToken(View):
    def get(self, request, **kwargs):
        if request.is_ajax():
            return HttpResponse("Token")
        else:
            return HttpResponse("No Token")

class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'user', 'app']

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title', 'secret', 'client_id', 'callbackUrl', 'scope', 'state']
    template_name_suffix = '_update_form'

class ProjectListView(ListView):

    model = Project
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
