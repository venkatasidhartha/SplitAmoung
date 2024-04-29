from django.urls import path
from . import views

urlpatterns = [
    path('updateprofile',views.update_profile)
]