from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ForgotPasswordForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Please , enter your email address',required=True)
    class Meta:
        model = User
        fields = ('email',)

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Please , enter a valid Email address',required=True)
    first_name = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=254)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
            )

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Please , enter a valid Email address',required=True)
    first_name = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=254)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            # 'password1',
            # 'password2'
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'dob',
            'gender',
            'nationality',
            'current_country',
            'user_state',
            'user_city',
            'address',
            'education',
            # 'association'
        )
        labels = {
            'dob': _("Date Of Birth"),
            'user_state': _("State"),
            'user_city': _("City"),
            'education': _("University / Institution")
        }
        widgets = {
            'dob': forms.TextInput(attrs={'placeholder': "Format: 'year-month-day'"}),
            # 'nationality': forms.TextInput(attrs={'placeholder': 'Your Country Name ...'}),
            # 'current_country': forms.TextInput(),
            # 'user_state': forms.TextInput(),
            # 'user_city': forms.TextInput(),
            # 'education': forms.TextInput()
            # 'identifier': forms.HiddenInput(attrs={'id': 'identifier_id'})
        }

        def __init__(self, *args, **kwargs):
            super(UserProfileForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)

            # self.helper.layout.append()
