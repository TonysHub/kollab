from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.apps.user.models import KollabUser
from django import forms


class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=KollabUser.Role.choices, required=True)

    class Meta:
        model = KollabUser
        fields = ("email", "first_name", "last_name", "username", "role")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = self.fields["role"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=25, required=True)
    password = forms.PasswordInput()
