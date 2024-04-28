from django.contrib import admin
from . import models
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id","email","name","created_at"]
    list_display_links = ["email"]
    list_filter = ["id","email","name"]
    search_fields = ["email","name"]


admin.site.register(models.User)
admin.site.register(models.Profile,ProfileAdmin)