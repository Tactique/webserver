from django.contrib import admin
from interface.models import GameUser, World, LoginData, ResponseTemplate

# Register your models here.
admin.site.register(GameUser)
admin.site.register(World)
admin.site.register(LoginData)
admin.site.register(ResponseTemplate)
