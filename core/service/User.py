from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from core import models
from core.response.signup import SignupResponse

class UserService:
    def create(self,obj):
        User = get_user_model()
        user = User.objects.create(email=obj.get_email())
        user.password = make_password(obj.get_password())
        user.save()
        response = SignupResponse()
        response.set_email(user.email)
        return response