from django.urls import path
from core import views


urlpatterns = [
    path('<str:code>/', views.RedirectView, name='redirect_view'),
    path('', views.HomeView, name="home_view"),
]   
