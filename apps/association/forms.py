from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

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

        def __init__(self, *args, **kwargs):
            super(AssociationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)

            # self.helper.layout.append()

        # Uin-form
        # helper = FormHelper()
        # helper.form_class = 'form-horizontal'
        # helper.layout = Layout(
        #     Field('name', css_class='input-xlarge'),
        #     Field('description', rows='3', css_class='input-xlarge')
        # )

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
