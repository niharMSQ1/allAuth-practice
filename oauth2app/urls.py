from django.urls import path
from .views import greet,dashboard

urlpatterns = [
    path('', greet),
    path('dashboard/',dashboard, name='dashboard' )
]