from django.urls import path
from core import views

urlpatterns = [
    path('<str:code>', views.Home, name='Home'),
    path('', views.Make, name="Make"),
]   