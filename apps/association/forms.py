from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AssociationForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = (
            'name',
            'description',
            'year_of_creation',
            'address',
            'phone',
            'initials',
            'country',
            'logo'
        )

class IdentifierForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        widgets = {
            'username': forms.HiddenInput()
        }
