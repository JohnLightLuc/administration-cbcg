# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class ProfesseurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'civilite',
        'fonction',
        'matiere',
        'enseignant',
        'matricule',
        'grade',
        'contact',
        'photo',
        'status',
        'date_add',
        'date_update',
        
    )
    list_filter = (
        'user',
        'civilite',
        'fonction',
        'matiere',
        'status',
        'date_add',
        'date_update',
    ) 


class CertificattravailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'prof',
        'nom',
        'prenom',
        'matricule',
        'emploi',
        'grade',
        'etat',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'prof',
        'status',
        'date_add',
        'date_update',
        
    )


class CertificatpriseserviceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'prof',
        'nom',
        'prenom',
        'matricule',
        'emploi',
        'grade',
        'etat',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = ( 
        'prof',
        'emploi',
        'grade',
        'etat',
        'status',
        'date_add',
        'date_update',
    )
    date_hierarchy = "date_update"
    search_fields = ['nom',]
    actions = ('active','desactive')


    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer certificats selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés certificats selectionnés"

class AttestationcongeAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'prof',
        'nom',
        'prenom',
        'fonction',
        'matricule',
        'datedebut',
        'datefin',
        'destination',
        'motif',
        'etat',
        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'nom',
        'status',
        'date_add',
        'date_update',
        
    )
    date_hierarchy = "date_update"

class NotificationAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'prof',
        'titre',
        'type_demande',
        'demande_id',

        'status',
        'date_add',
        'date_update',
    )
    list_filter = (
        'titre',
        'status',
        'date_add',
        'date_update',
        
    )
    date_hierarchy = "date_update"

 
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Professeur, ProfesseurAdmin)
_register(models.Certificattravail, CertificattravailAdmin)
_register(models.Certificatpriseservice, CertificatpriseserviceAdmin)
_register(models.Attestationconge, AttestationcongeAdmin)
_register(models.Notification, NotificationAdmin)
