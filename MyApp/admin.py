from django.contrib import admin
from django.contrib.auth.models import User
from .models import Help
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class HelpInLine(admin.StackedInline):
    model = Help
    can_delete = False
    verbose_name_plural = 'Help'

class CustomizedUserAdmin (UserAdmin):
    inlines = (HelpInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Help)