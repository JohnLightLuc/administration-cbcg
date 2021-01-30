# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class AdministrationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'civilite',
        'fonction',
        'contact',
        'grade',
        'matricule',
        'photo',
        'status',
        'date_add',
        'date_update',
        
    )
    list_filter = (
        'user',
        'civilite',
        'fonction',
    ) 
    date_hierarchy = "date_update"
    search_fields = ['fonction',]
    actions = ('active','desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request,"La selection a été activé avec succés")
        
    active.short_description = "activer les administarteurs selectionnés"
        
        
    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request,"La selection a été desactivé avec succés")
            
    desactive.short_description = "desactivés les administarteurs selectionnés"

       
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Administration, AdministrationAdmin)
