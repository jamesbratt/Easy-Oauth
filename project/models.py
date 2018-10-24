from django.urls import reverse
from django.db import models
from customuser.models import LeftfootUser
    
STRAVA = 'SA'

APP_CHOICES = (
    (STRAVA, 'Strava'),
)

class Project(models.Model):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(LeftfootUser, on_delete=models.CASCADE)
    app = models.CharField(
        max_length=2,
        choices=APP_CHOICES,
    )
    secret = models.TextField()
    client_id = models.CharField(max_length=100)
    callbackUrl = models.TextField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self,):
        return reverse('project:update-project', kwargs={'pk': self.pk})
