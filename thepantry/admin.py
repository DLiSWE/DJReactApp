from django.contrib import admin
from . import models
# Register your models here.
class ThepantryAdmin(admin.ModelAdmin):
    search_fields = ['item']


admin.site.register(models.MyPantry, ThepantryAdmin)