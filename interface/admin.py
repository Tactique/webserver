from django.contrib import admin
from interface.models import GameUser, World, LoginData

# Register your models here.
admin.site.register(GameUser)
admin.site.register(World)
admin.site.register(LoginData)
