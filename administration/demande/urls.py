"""administration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name ="demande"

urlpatterns = [
    path('connexion', views.connexion, name="connexion"),
    path('home', views.home, name="index"),
    path('compte/', views.compte, name="compte"),
    path('<int:id>/annule_conge/', views.annuleconge, name="annuleconge"),
    path('<int:id>/annule_travail/', views.annuletravail, name="annuletravail"),
    path('<int:id>/annule_service/', views.annuleservice, name="annuleservice"),
    path('attestation_de_conge/', views.attestation_conge, name="attestation"),
    path('update/', views.modify, name="update"),
    path('service/', views.service, name="service"),
    path('travail/', views.travail, name="travail"),
    path('logout/', views.deconnexion, name="logout"),

    
]
