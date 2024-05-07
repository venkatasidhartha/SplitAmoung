from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup),
    path('getprofile',views.get_profile),
    path('updateprofile',views.update_profile),
    path('uploadprofile_pic',views.upload_profile_pic),
    path('getprofilepic',views.get_profile_pic)
]