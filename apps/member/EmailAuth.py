'''
from django.contrib.auth.models import User

class EmailBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        #except User.MultipleObjectsReturned:
            #user = User.objects.filter(email=username).order_by('id').first
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
'''

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class EmailBackend(object):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            raise ValidationError("Invalid credentials")

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
