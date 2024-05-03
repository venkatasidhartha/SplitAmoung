from django.contrib import admin
from . import models
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id","email","name","created_at"]
    list_display_links = ["email"]
    list_filter = ["id","email","name"]
    search_fields = ["email","name"]

class S3FileAdmin(admin.ModelAdmin):
    list_display = ["id","table_name","created_at"]
    list_display_links = ["table_name"]
    list_filter = ["id","table_name","table_field"]
    search_fields = ["table_name","table_field"]

admin.site.register(models.User)
admin.site.register(models.Profile,ProfileAdmin)
admin.site.register(models.S3_File,S3FileAdmin)