from django.contrib import admin
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Appareil,Hopital, Patient, Service, Medecin
from django.utils.safestring import mark_safe
# Register your models here.


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class MedecinInline(admin.TabularInline):
    model = Medecin
    extra = 1

class AppareilInline(admin.TabularInline):
    model = Appareil
    extra = 1




class AppareilAdmin(admin.ModelAdmin):

    # Liste des attributs à afficher dans la liste des utilisateurs
    list_display = ['nom']

    # Champs de recherche pour le panneau d'administration
    search_fields = ['nom']

    list_filter = [ 'nom']

    list_per_page = 10
admin.site.register(Appareil, AppareilAdmin)

class MedecinAdmin(admin.ModelAdmin):

    # Liste des attributs à afficher dans la liste des utilisateurs
    list_display = ['nom', 'titre', 'tel', 'photo']

    # Champs de recherche pour le panneau d'administration
    search_fields = ['nom', 'titre', 'photo']

    list_filter = [ 'nom', 'titre', 'photo']

    list_per_page = 10
admin.site.register(Medecin, MedecinAdmin)

class PatientAdmin(admin.ModelAdmin):

    # Liste des attributs à afficher dans la liste des utilisateurs
    list_display = ['nom', 'email', 'tel', 'service', 'date', 'recu']

    # Champs de recherche pour le panneau d'administration
    search_fields = ['nom', 'email', 'tel']

    list_filter = [ 'nom', 'email', 'tel']

    list_per_page = 10
admin.site.register(Patient, PatientAdmin)




class ServiceAdmin(admin.ModelAdmin):

    inlines = [MedecinInline, AppareilInline]
 
    # Liste des attributs à afficher dans la liste des utilisateurs
    list_display = ['__str__', 'liste_des_appareils']

    # Champs de recherche pour le panneau d'administration
    search_fields = ['nom']

    list_filter = [ 'nom']

    list_per_page = 10

    def liste_des_appareils(self, obj):
        return ", ".join([str(s.nom) for s in obj.appareils.all()])
    
admin.site.register(Service, ServiceAdmin)

class HopitalAdmin(admin.ModelAdmin):
    
    inlines = [ServiceInline]

    # Liste des attributs à afficher dans la liste des utilisateurs
    list_display = ['nom', 'liste_service']

    # Champs de recherche pour le panneau d'administration
    search_fields = ['nom']

    list_filter = [ 'nom']

    list_per_page = 10

    
    def liste_service(self, obj):
        services_html = ""
        for service in obj.services.all():
            en_operation_icon = '<a href="{}"><i class="fas fa-play"></i></a>'.format(reverse('mettre_en_operation', args=[service.id]))
            hors_operation_icon = '<a href="{}"><i class="fas fa-pause"></i></a>'.format(reverse('mettre_hors_operation', args=[service.id]))
            action_icon = hors_operation_icon if service.en_operation else en_operation_icon
            # Ajouter des espaces entre le texte du service et l'icône
            service_html = "<div style='display: inline-block;'>{}</div>&nbsp;&nbsp;&nbsp;<div style='display: inline-block;'>{}</div><br>".format(service.nom, format_html(action_icon))
            services_html += service_html
        return format_html(services_html)
    liste_service.short_description = "Services"
    
admin.site.register(Hopital, HopitalAdmin)



