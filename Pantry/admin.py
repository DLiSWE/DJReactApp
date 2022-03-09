from django.contrib import admin
from . import models
# Register your models here.
class PantryAdmin(admin.ModelAdmin):
    search_fields = ['item']


admin.site.register(models.myPantry, PantryAdmin)