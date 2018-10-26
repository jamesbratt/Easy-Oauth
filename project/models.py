from django.urls import reverse
from django.db import models
from customuser.models import LeftfootUser
from integration_config.models import IntegrationConf

class Project(models.Model):
    """ A developers project for a particular integration """

    title = models.CharField(max_length=100)
    user = models.ForeignKey(LeftfootUser, on_delete=models.CASCADE)
    integration = models.ForeignKey(IntegrationConf, on_delete=models.SET_NULL, null=True)
    secret = models.TextField()
    client_id = models.CharField(max_length=100)
    callbackUrl = models.TextField()
    scope = models.TextField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self,):
        """ To return to update page when resource is craeted or modified """
        return reverse('project:update-project', kwargs={'pk': self.pk})
