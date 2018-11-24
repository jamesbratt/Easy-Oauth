from django.forms import ModelForm
from project.models import Project

class TwitterForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'callbackUrl', 'oauth_consumer_key']
