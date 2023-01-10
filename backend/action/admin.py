from django.contrib import admin

from action.models import (
    Subscription, 
    Like, 
    Dislike,
    View
)

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(View)
