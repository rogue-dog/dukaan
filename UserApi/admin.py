from django.contrib import admin

from UserApi.models import Item, User

# Register your models here.
admin.site.register(User)
admin.site.register(Item)
