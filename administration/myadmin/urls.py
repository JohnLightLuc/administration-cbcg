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

app_name ="myadmin"

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>/delete_attestation_conge', views.supprimerConge, name="supconge"),
    path('<int:id>/delete_certificat_travail', views.supprimertravail, name="suptraval"),
    path('<int:id>/delete_certificat_service', views.supprimerservice, name="supservice"),
    path('compte/', views.compte, name="compte"),
    path('<int:id>/attestation_de_conge/', views.attestation_conge, name="attestationconge"),
    path('<int:id>/attestation_de_travail/', views.attestation_travail, name="attestationtravail"),
    path('<int:id>/certificat_de_reprise_de_service/', views.certificat_service, name="certificatservice"),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="logout"),
    path('<int:id>/delete_notification', views.deletenotification, name="deletenotification"),
    path('delete_all_notification', views.delete_all_notification, name="alldelete"),

    
]
