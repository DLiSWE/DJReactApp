from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, FormView
# from .forms import SignupForm, EditForm, ProfileUpdateForm
from django.contrib.auth import get_user_model
from Pantry.forms import addToPantry, PantryForm
from . import models

# Create your views here.
class AllIngredients(ListView,LoginRequiredMixin):
    model = models.Ingredients
    template_name = 'ingredients.html'

    def get_queryset(self, *args, **kwargs):
        query = super(AllIngredients, self).get_queryset(*args, **kwargs)
        query = query.order_by("id")
        return query

class my_Pantry(ListView,LoginRequiredMixin):
    model = models.myPantry
    template_name = 'pantry.html'

class ingredientFormView(CreateView, LoginRequiredMixin):
    template_name = 'ingredients.html'
    form_class = addToPantry
    success_url = reverse_lazy('Pantry:pantry_list')

    def get_success_url(self):
        return reverse_lazy

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.pantry_id = self.kwargs.get('pk')
        print(self.request)
        self.object.save()
        return super().form_valid(form)

class CreatePantry(CreateView, LoginRequiredMixin):
    template_name = 'mypantry_form.html'
    form_class = PantryForm
    success_url = reverse_lazy('Pantry:pantry_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.pantry_id = self.kwargs.get('pk')
        print(self.request)
        self.object.save()
        return super().form_valid(form)
