from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('date', views.date_actuelle),
    path('somme/<int:nombre1>/<int:nombre2>/', views.somme)
]
