from django.contrib import admin

from .models import ForumDB, ThreadDB

# Register your models here.

admin.site.register(ForumDB)
admin.site.register(ThreadDB)

