from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # Additional field to the form
    email = forms.EmailField()

    class Meta:
        # Save the user to this model
        model = User
        # Order of the fields to be shown
        fields = ['username', 'email', 'password1', 'password2']
