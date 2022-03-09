from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from thepantry.models import PantryModel

app_name = 'thepantry'

urlpatterns = [
    # path('ingredients/', views.AllIngredients.as_view(), name='ingredients'),
    path('', views.my_Pantry.as_view(), name='pantry_list'),
    path('add/<int:pk>', views.ingredientFormView.as_view(),name='ingredients'),
    path('create/<int:pk>', views.CreatePantry.as_view(),name='create'),
    path('my/<int:pk>', views.SinglePantryView.as_view(model=PantryModel),name='single'),
    # path('<int:pk>/', views.deletePantryView.as_view(), name='pantry_delete')
    # path('ingredients/<int:pk>')
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)