from django.urls import reverse
from django.db import models

class IntegrationConf(models.Model):
    """ To link projects to integration modules """

    title = models.CharField(max_length=100)
    module_path = models.CharField(max_length=100)
    oauth_class_name = models.CharField(max_length=100)
    form_class_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self,):
        """ To return to update page when resource is craeted or modified """
        return reverse('integrations:update-integration', kwargs={'pk': self.pk})
