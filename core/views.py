from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from core.utility import capture_error
# Create your views here.

# Importing Request
from core.request.signup import SignupRequest
from core.request.profile import ProfileRequest 

# Importing Service
from core.service.User import UserService
from core.service.Profile import ProfileService

# Importing Common Response
from core.common.response import CommonResponse



"""
Create user code

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.create(email="user1@user.com")
user.password = make_password('admin')
user.save()
"""

@api_view(['POST'])
@permission_classes([AllowAny])
@capture_error
def signup(request):
    request_data = SignupRequest(request.data)
    service = UserService()
    user_response = service.create(request_data)
    response = CommonResponse(message="created successfully",data=user_response.get_obj(),status_code=201).get_response()
    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@capture_error
def get_profile(request):
    service = ProfileService()
    profile_response = service.read(request.user)
    response = CommonResponse(message="success",data=profile_response.get_dict()).get_response()
    return response



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@capture_error
def update_profile(request):
    request_data = ProfileRequest(request.data)
    service = ProfileService()
    profile_response = service.update(request_data,request.user)
    response = CommonResponse(message="success",data=profile_response.get_dict()).get_response()
    return response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@capture_error
def upload_profile_pic(request):
    if "image" not in request.FILES:
        raise ValueError("image is requied")
    service = ProfileService()
    profile_response = service.uploadProfilepic(request)
    response = CommonResponse(message="success",data=profile_response.get_dict()).get_response()
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@capture_error
def get_profile_pic(request):
    service = ProfileService()
    return service.getProfilePic(request.user) 
