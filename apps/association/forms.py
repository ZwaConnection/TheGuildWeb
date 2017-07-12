from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

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
        labels = {
            'name': _("Association name")
        }

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
            'username': forms.HiddenInput(attrs={'id': 'association_id'})
        }
