from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from core.utility import extract_username_from_email
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)

# custom user model 
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()



class Profile(models.Model):
    email = models.EmailField(_("email address"), unique=True,blank=False)
    name = models.CharField(max_length=255,blank=False)
    phone = models.CharField(max_length=50,blank=True)
    profile_pic_s3 = models.IntegerField(blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwards):
    user = instance
    if created and not user.is_superuser and not user.is_staff:
        profile = Profile.objects.create(
            email=user.email,
            name=extract_username_from_email(user.email),
            user=user
        )

class S3_File(models.Model):
    url = models.URLField(max_length=255,blank=False,null=False) 
    app_name = models.CharField(max_length=100,blank=False,null=False)
    table_name = models.CharField(max_length=100,blank=False,null=False)
    table_field = models.CharField(max_length=100,blank=False,null=False)
    user_id = models.IntegerField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.table_name