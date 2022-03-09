from django.contrib.auth import get_user_model
from django import forms
from thepantry.models import myPantry, PantryModel
from django.conf import settings

class addToPantry(forms.ModelForm):
    class Meta:
        model = myPantry
        fields = ('item','pantry_id')

class PantryForm(forms.ModelForm):
    class Meta:
        model = PantryModel
        fields = ('name',)
        widgets = {
            'name':forms.TextInput()
        }

       


        