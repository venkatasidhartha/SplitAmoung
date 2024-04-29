from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.utility import capture_error
# Create your views here.

# importing request
from core.request import profile 

# importing service
from core.service.Profile import ProfileService

# importing response
from core.response.generic import Response

@api_view(['POST'])
@capture_error
def update_profile(request):
    print(request.data)
    request_data = profile.Request(request.data)
    service = ProfileService()
    service.update(request_data)
    response = Response(data=["sidhu"])#
    print(response())
    return JsonResponse(response())