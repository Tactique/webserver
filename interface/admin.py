from django.contrib import admin
from interface.models import GameUser, Cell, Unit, World

# Register your models here.
admin.site.register(GameUser)
admin.site.register(Cell)
admin.site.register(Unit)
admin.site.register(World)