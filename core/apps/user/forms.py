from django.contrib.auth.forms import UserCreationForm
from core.apps.user.models import KollabUser
from django import forms


class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=KollabUser.Role.choices, required=True)

    class Meta(UserCreationForm.Meta):
        model = KollabUser
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "role",
            "profile_image",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = self.fields["role"]

