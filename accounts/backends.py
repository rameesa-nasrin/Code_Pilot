from django.contrib.auth.backends import BaseBackend

from accounts.models import User

class EmailBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try:

            user_object = User.objects.get(email=username)

            if user_object.check_password(password):

                return user_object

            else:

                return None

        except:

            return None


class PhoneBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try:

            user_object = User.objects.get(phone=username)

            if user_object.check_password(password):

                return user_object

            else:

                return None

        except:

            return None
