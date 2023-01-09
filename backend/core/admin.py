from django.contrib import admin

from core.models import Channel, Category, Content
# Register your models here.

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Content)
