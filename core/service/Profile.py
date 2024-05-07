from django.db.models import Q
from django.http import HttpResponse
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
        profile = models.Profile.objects.get(user__id=request.user.id)
        file_name = file_obj.name
        SupportedimagesExtension = Extensions().image
        if extract_file_extenstion(file_name) not in SupportedimagesExtension:
            raise Exception("Unsupported file")
        fileservice = FileService()
        s3obj = fileservice.uploadToS3(
            request=request,
            key="image",
            table_name="Profile",
            table_field="profile_pic_s3",
            path_to_store=f"{profile.email}/profile/",
        )
        profile.profile_pic_s3 = s3obj.id
        profile.save()
        response = ProfileResponse()
        response.set_message("uploaded")
        response.set_s3_id(s3obj.id) 
        response.set_s3_url(s3obj.url)
        return response

    def getProfilePic(self,user):
        profile = models.Profile.objects.get(user__id=user.id)
        fileservice = FileService()
        file_content = fileservice.get_s3File(profile.profile_pic_s3)
        return file_content

