from django.contrib.auth import get_user_model
from django import forms
from thepantry.models import MyPantry, PantryModel
from Account.models import EndUser
from django.conf import settings

class addToPantry(forms.ModelForm):
    class Meta:
        model = MyPantry
        fields = ('item','pantry_id')

    def __init__(self, *args,**kwargs):
        request = kwargs.pop("request", None)
        user = request.user.id
        super().__init__(*args,**kwargs)
        if user is not None:
            self.fields['pantry_id'].queryset = PantryModel.objects.filter(user=user)



class PantryForm(forms.ModelForm):
    class Meta:
        model = PantryModel
        fields = ('name',)
        widgets = {
            'name':forms.TextInput()
        }

       


        