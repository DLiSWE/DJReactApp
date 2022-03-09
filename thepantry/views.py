from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, FormView
# from .forms import SignupForm, EditForm, ProfileUpdateForm
from django.http import Http404, HttpResponseRedirect
from thepantry.forms import addToPantry, PantryForm
from . import models
from thepantry.models import Ingredients, myPantry, PantryModel
from django.utils.text import slugify

# Create your views here.
class AllIngredients(ListView,LoginRequiredMixin):
    model = models.Ingredients
    template_name = 'ingredients.html'

    def get_queryset(self, *args, **kwargs):
        query = super(AllIngredients, self).get_queryset(*args, **kwargs)
        query = query.order_by("id")
        return query

class my_Pantry(ListView,LoginRequiredMixin):
    model = models.PantryModel
    template_name = 'pantry.html'
    context_object_name = 'pantryList'

    def get_context_data(self,**kwargs):
        context = super(my_Pantry, self).get_context_data(**kwargs)
        context['fields'] = [field.name for field in models.PantryModel._meta.get_fields()]
        return context

class ingredientFormView(CreateView, LoginRequiredMixin):
    template_name = 'ingredients.html'
    form_class = addToPantry
    success_url = reverse_lazy('thepantry:pantry_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        item_id = form.cleaned_data['item']
        item_name = Ingredients.objects.all().filter(ingredient_name=item_id)[0]
        pantry_id = form.cleaned_data['pantry_id']
        pantry_name = PantryModel.objects.all().filter(name=pantry_id)[0]
        slug = slugify(pantry_name)
        self.object.pantry_name = pantry_name
        self.object.slug = slug
        self.object.item_name = item_name
        self.object.pantry_id = pantry_id
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)

class CreatePantry(CreateView, LoginRequiredMixin):
    template_name = 'mypantry_form.html'
    form_class = PantryForm
    success_url = reverse_lazy('thepantry:pantry_list')

    def form_valid(self, form):
        self.pantry = form.save(commit=False)
        pantry_name = form.cleaned_data['name']
        slug = slugify(pantry_name)
        self.pantry.pantry_name = pantry_name
        self.pantry.user = self.request.user
        self.pantry.slug = slug
        self.pantry.save()
        return super().form_valid(form)


class SinglePantryView(DetailView):
    model = PantryModel
    template_name = 'pantry_detail.html'
