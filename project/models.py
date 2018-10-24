from django.urls import reverse
from django.db import models
from customuser.models import LeftfootUser
from integrations.registry import REGISTRY
    
APP_CHOICES = []

for registeredApp in REGISTRY.keys():
    APP_CHOICES.append((registeredApp, registeredApp))

class Project(models.Model):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(LeftfootUser, on_delete=models.CASCADE)
    app = models.CharField(
        max_length=30,
        choices=APP_CHOICES,
    )
    secret = models.TextField()
    client_id = models.CharField(max_length=100)
    callbackUrl = models.TextField()
    scope = models.TextField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self,):
        return reverse('project:update-project', kwargs={'pk': self.pk})
