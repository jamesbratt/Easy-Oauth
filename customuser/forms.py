from django.contrib.auth.forms import UserCreationForm
from .models import EasyOauthUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = EasyOauthUser
        fields = ("username", "email", )
