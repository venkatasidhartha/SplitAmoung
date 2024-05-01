from django.db.models import Q
from core import models 
from core.response.profile import ProfileResponse


class ProfileService:
    
    def read(self,user):
        profile = models.Profile.objects.get(user__id=user.id)
        response = ProfileResponse()
        response.set_email(profile.email)
        response.set_name(profile.name)
        response.set_phone(profile.phone)
        return response

    
    def update(self,obj,user):
        profile = models.Profile.objects.get(user__id=user.id)
        if obj.get_email() != None:
            user_instance = profile.user
            user_instance.email = obj.get_email()
            user_instance.save()
            profile.email = obj.get_email()
        if obj.get_name() != None:
            profile.name = obj.get_name()
        if obj.get_phone() != None:
            profile.phone = obj.get_phone()
        profile.save()

        response = ProfileResponse()
        response.set_email(profile.email)
        response.set_name(profile.name)
        response.set_phone(profile.phone)
        return response
        