from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignupForm, EditForm, ProfileUpdateForm
from django.contrib.auth import get_user_model

#C,U,U,D
# Create your views here.
class SignUp(CreateView):
    model = get_user_model()
    form_class = SignupForm
    template_name = 'Account/signup.html'
    success_url = reverse_lazy('login')

class EditUser(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    form_class = EditForm
    template_name = 'Account/edit_user.html'
    success_url = reverse_lazy('Groups:all')

class UpdateProfile(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    form_class = ProfileUpdateForm
    template_name = 'Account/edit_profile.html'
    success_url = reverse_lazy('Groups:all')

class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'Account/profile_page.html'
    
