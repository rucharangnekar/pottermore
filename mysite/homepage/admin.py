from django.contrib import admin

# Register your models here.
from .models import Myusr, Profile


admin.site.register(Myusr)
admin.site.register(Profile)

