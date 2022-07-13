from django.urls import path
from . import views

urlpatterns = [
    path('mesures', views.get_data),
    path('add/', views.add_mesure)
]