from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.apps.user.models import KollabUser
from django import forms


class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=KollabUser.Role.choices, required=True)

    class Meta:
        model = KollabUser
        fields = ("email", "first_name", "last_name", "username", "role")

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'field--l'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['email'].widget.attrs['required'] = 'true'

        self.fields['first_name'].widget.attrs['class'] = 'field--l'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['first_name'].widget.attrs['required'] = 'true'

        self.fields['last_name'].widget.attrs['class'] = 'field--l'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['last_name'].widget.attrs['required'] = 'true'

        self.fields['username'].widget.attrs['class'] = 'field--l'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['username'].widget.attrs['required'] = 'true'

        self.role = self.fields["role"]
        self.fields['role'].widget.attrs['class'] = 'field--l'
        self.fields['role'].widget.attrs['placeholder'] = 'Select your role'
        self.fields['role'].widget.attrs['required'] = 'true'

        self.fields['password1'].widget.attrs['class'] = 'field--l'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password1'].widget.attrs['required'] = 'true'

        self.fields['password2'].widget.attrs['class'] = 'field--l'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password again'
        self.fields['password2'].widget.attrs['required'] = 'true'


        
        


