import json
from importlib import import_module
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from project.models import Project
from integration_config.models import IntegrationConf

def get_integration(integration_id):
    """ Getting the integration config from db """
    integration = IntegrationConf.objects.get(pk=integration_id)
    oauth_class_name = integration.oauth_class_name
    form_class_name = integration.form_class_name
    integration_module_path = integration.module_path

    oauth_class = getattr(import_module(integration_module_path), oauth_class_name)
    form_class = getattr(import_module(integration_module_path), form_class_name)

    return {'oauthClass': oauth_class, 'formClass': form_class}

class OauthLoginRedirect(View):
    """ Redirect to an integrations authorization page """

    def get(self, request, **kwargs):
        """ Get the redirect url """
        fields = Project.objects.get(pk=self.kwargs['pk'])
        integration = get_integration(fields.integration.pk)
        integration_instance = integration['oauthClass'](fields)
        url = integration_instance.get_auth_url()

        return HttpResponseRedirect(url)

class GetOauthToken(View):
    """ Get authorisation response from an integration """

    def get(self, request, **kwargs):
        """ Getting the token """
        oauth_response = None
        status_code = 200

        params = request.GET
        fields = Project.objects.get(pk=self.kwargs['pk'])
        integration = get_integration(fields.integration.pk)
        integration_instance = integration['oauthClass'](fields)

        try:
            oauth_response = integration_instance.get_auth_response(params)
        except ValueError as err:
            oauth_response = err.args[0]
            status_code = 400

        response = HttpResponse(json.dumps(oauth_response))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        response.status_code = status_code
        return response

class ProjectCreate(CreateView):
    """ Creating a new project """

    model = Project
    fields = ['title', 'user', 'integration']

class ProjectUpdate(UpdateView):
    """ Updating an existing project """

    model = Project
    form_class = None
    template_name_suffix = '_update_form'


    def dispatch(self, request, *args, **kwargs):
        fields = Project.objects.get(pk=self.kwargs['pk'])
        integration = get_integration(fields.integration.pk)
        integration_form_class = integration['formClass']
        self.form_class = integration_form_class
        return super(ProjectUpdate, self).dispatch(request, *args, **kwargs)

class ProjectListView(ListView):
    """ Listing all projects """

    model = Project
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """ Returning context """
        context = super().get_context_data(**kwargs)
        return context
