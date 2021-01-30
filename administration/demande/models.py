from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Professeur(models.Model):
    # Appel de user

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeur')  

    # Champs suplementaires

    civilite = models.CharField(max_length=50)
    fonction = models.CharField(max_length=255)
    matiere = models.CharField(max_length=255)
    enseignant = models.IntegerField(default=1)
    matricule = models.CharField(max_length=30)
    grade = models.CharField(max_length=10)
    contact = models.CharField(max_length=30, null=True)
    annee_de_prise_de_travail = models.CharField(max_length=225, null=True)
    photo = models.ImageField(upload_to='administrateur/', default='useravatar.png')

    status = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    

class Certificattravail(models.Model):
    """Model definition for Certificattravail."""

    # TODO: Define fields here
    prof = models.ForeignKey(Professeur, related_name='travailprof', on_delete=models.CASCADE)  

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    matricule = models.CharField(max_length=255)
    emploi = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    etat = models.CharField(max_length=255,default="En attente",   
        choices=[
            ('En attente', 'En attente'),
            ('Traité', 'Traité'),
            ('Annulé', 'Annulé')
        ]
    ) 

    
    status = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Certificattravail."""

        verbose_name = 'Certificat de travail'
        verbose_name_plural = 'Certificats de travail'

    def __str__(self):
        """Unicode representation of Certificattravail."""
        return self.nom


class Certificatpriseservice(models.Model):
    """Model definition for Certificatprisetravail."""

    # TODO: Define fields here
    prof = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='priseserviceprof')  

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    matricule = models.CharField(max_length=255)
    emploi = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    etat = models.CharField(max_length=255,default="En attente",   
        choices=[
            ('En attente', 'En attente'),
            ('Traité', 'Traité'),
            ('Annulé', 'Annulé')
        ] 
    )
    
    status = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Certificatpriseservice."""

        verbose_name = 'certificat de prise de service'
        verbose_name_plural = 'certificats de prise de service'

    def __str__(self):
        """Unicode representation of Certificatpriseservice."""
        return self.nom


class Attestationconge(models.Model):
    """Model definition for AAttestationconge."""

    # TODO: Define fields here
    prof = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='congeprof')  


    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    matricule = models.CharField(max_length=255)
    datedebut =  models.DateField()
    datefin =  models.DateField()
    destination = models.CharField(max_length=255)
    motif = models.CharField(max_length=255)
    etat = models.CharField(max_length=255,default="En attente",   
        choices=[
            ('En attente', 'En attente'),
            ('Traité', 'Traité'),
            ('Annulé', 'Annulé')
        ] 
    )

    
    status = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Attestationconge."""

        verbose_name = 'attestation de congé'
        verbose_name_plural = 'attestations de congé'

    def __str__(self):
        """Unicode representation of Attestationconge."""
        return self.nom

class Notification(models.Model):
    """Model definition for Notification."""

    # TODO: Define fields here
    prof = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='notiprof')  

    titre = models.CharField(max_length=255)
    type_demande = models.CharField(max_length=255, choices=[
        ('travail', 'travail'),
        ('service', 'service'),
        ('conge', 'conge')
    ])
    demande_id = models.IntegerField()

    status = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Notification."""

        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        """Unicode representation of Notification."""
        return self.titre
