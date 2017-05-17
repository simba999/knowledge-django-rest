import uuid
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import authentication
from api.models import User
from django.http import Http404
from rest_framework import exceptions
from django.views.decorators.csrf import csrf_exempt
import pdb


def get_user_by_name(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        pass
        # raise exceptions.AuthenticationFailed('No such user')


class ExampleAuthentication(authentication.BaseAuthentication):
    print "***** Example authentication *********"
    def authenticate(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print "Username: ", username
        print "password: ", password
        user = get_user_by_name(username)
        # print password
        try:
            pwd_valid = check_password(password, user.password)
        except:
            return (user, None)
        print "valid: ", pwd_valid
        if pwd_valid:
            user.remember_token = uuid.uuid4()
            # user.is_authenticated = True
            user.save()

        return (user, None) # authentication successful