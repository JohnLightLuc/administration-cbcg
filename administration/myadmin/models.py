from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Administration(models.Model):
    # Appel de user

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrateur')  

    # Champs suplementaires

    civilite = models.CharField(max_length=50)
    fonction = models.CharField(max_length=225)
    contact = models.CharField(max_length=30, null=True)
    grade = models.CharField(max_length=10)
    matricule = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='myadmin/', default='useravatar.png')

    status = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    