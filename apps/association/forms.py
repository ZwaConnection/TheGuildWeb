from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


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


class AssociationForm(forms.ModelForm):
    class Meta:
        model = Association
        # exclude = ['identifier']
        fields = (
            'name',
            'description',
            'year_of_creation',
            'address',
            'phone',
            'initials',
            'country',
            # 'logo',
            # 'identifier'
        )
        labels = {
            'name': _("Association name"),
            'year_of_creation': _('Date of Creation')
        }
        widgets = {
            'year_of_creation': forms.TextInput(attrs={'placeholder': "Format: 'year-month-day'"}),
            # 'identifier': forms.HiddenInput(attrs={'id': 'identifier_id'})
        }

        def __init__(self, *args, **kwargs):
            super(AssociationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)

            # self.helper.layout.append()
