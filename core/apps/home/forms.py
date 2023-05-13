from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.apps.user.models import KollabUser

class SignUpForm(UserCreationForm):
    

    class Meta:
        model = KollabUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )