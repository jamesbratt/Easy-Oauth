import json
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from project.models import Project
from integrations.registry import get_integration_from_registry


class OauthLoginRedirect(View):
    """ Redirect to an integrations authorization page """

    def get(self, request, **kwargs):
        """ Get the redirect url """
        fields = Project.objects.get(pk=self.kwargs['pk'])
        integration = get_integration_from_registry(fields.app)
        integration_instance = integration(fields)
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
        integration = get_integration_from_registry(fields.app)
        integration_instance = integration(fields)

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
    fields = ['title', 'user', 'app']

class ProjectUpdate(UpdateView):
    """ Updating an existing project """

    model = Project
    fields = ['title', 'secret', 'client_id', 'callbackUrl', 'scope', 'state']
    template_name_suffix = '_update_form'

class ProjectListView(ListView):
    """ Listing all projects """

    model = Project
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """ Returning context """
        context = super().get_context_data(**kwargs)
        return context
