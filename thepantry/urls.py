from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from thepantry.models import PantryModel

app_name = 'thepantry'

urlpatterns = [
    path('explore', views.AllPantry.as_view(), name='all'),
    path('', views.my_Pantry.as_view(), name='pantry_list'),
    path('add/<int:pk>', views.ingredientFormView.as_view(),name='ingredients'),
    path('create/<int:pk>', views.CreatePantry.as_view(),name='create'),
    path('delete/<int:pk>/', views.DeletePantry.as_view(), name='pantry_delete'),
    path('view/<str:slug>/', views.PantryDetails.as_view(), name='single'),
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)