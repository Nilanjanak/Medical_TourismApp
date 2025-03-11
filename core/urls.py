# urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('location/', views.location_view, name='location'),
    path('get_states/', views.get_states, name='get_states'),
]
