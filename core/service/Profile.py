from django.db.models import Q
from core import models 



class ProfileService:
    
    def read(self,user):
        pass
    
    def update(self,obj):
        condition = Q(email=obj.get_email())
        if obj.get_name() != None:
            condition&=Q(name=obj.get_name())
        if obj.get_phone() != None:
            condition&=Q(phone=obj.get_phone())
        print(condition)
        