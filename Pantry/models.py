from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Ingredients(models.Model):
    ingredient_name = models.TextField(db_column='Ingredient Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.TextField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredients'

    def __str__(self):
        return self.ingredient_name

class myPantry(models.Model):
    id = models.IntegerField(blank=True,null=True)
    item = models.ForeignKey(Ingredients,related_name='ingredientIn',on_delete = models.CASCADE, blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_pantry', on_delete = models.CASCADE,blank=True,null=True)

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)

class PantryModel(models.Model):
    name = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='single_pantry', on_delete = models.CASCADE,blank=True,null=True)
