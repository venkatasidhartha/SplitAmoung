from django.urls import path
from . import views

urlpatterns = [
    path('getprofile',views.get_profile),
    path('updateprofile',views.update_profile)
]