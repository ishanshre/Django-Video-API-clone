from django.contrib import admin

from action.models import (
    Subscription, 
    Like, 
    Dislike
)

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Like)
admin.site.register(Dislike)
