from django.db.models import Q
from core import models
from core.response.profile import ProfileResponse
from core.file_extensions import Extensions
from core.utility import extract_file_extenstion
from core.service.File import FileService
from uuid import uuid4

class ProfileService:

    def read(self, user):
        profile = models.Profile.objects.get(user__id=user.id)
        response = ProfileResponse()
        response.set_email(profile.email)
        response.set_name(profile.name)
        response.set_phone(profile.phone)
        return response

    def update(self, obj, user):
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

    def uploadProfilepic(self, request):
        file_obj = request.FILES["image"]
        user_obj = request.user
        module_name = request.resolver_match.func.__module__
        app_name = module_name.split(".")[0]
        profile = models.Profile.objects.get(user__id=user_obj.id)
        file_name = file_obj.name
        SupportedimagesExtension = Extensions().image
        if extract_file_extenstion(file_name) not in SupportedimagesExtension:
            raise Exception("Unsupported file")
        fileservice = FileService()
        s3obj = fileservice.upload(
            user_id=user_obj.id,
            app_name=app_name,
            table_name="Profile",
            table_field="profile_pic_s3",
            file=file_obj,
            path_to_store=f"{profile.email}/profile/{str(uuid4())}/{file_name}",
        )
        profile.profile_pic_s3 = s3obj.id
        profile.save()

        response = ProfileResponse()
        response.set_message("uploaded")
        response.set_s3_id(s3obj.id) 
        response.set_s3_url(s3obj.url)
        return response

