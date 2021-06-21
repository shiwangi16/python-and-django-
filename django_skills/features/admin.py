from django.contrib import admin
from features.models import Info
# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    list_display = ["names", "contact","interests"]

admin.site.register(Info, InfoAdmin)