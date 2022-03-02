from django.urls import path
from .views import index

app_name = 'frontend'

#add url patterns

urlpatterns = [
    path('', index, name=''),
]