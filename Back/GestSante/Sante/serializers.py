from rest_framework import serializers
from .models import Appareil, Hopital, Medecin, Patient, Service

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = ['id', 'nom', 'titre', 'tel', 'photo']

class AppareilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appareil
        fields = ['id', 'nom']

class ServiceSerializer(serializers.ModelSerializer):
    medecins = MedecinSerializer(many=True, read_only=True)
    appareils = AppareilSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'nom', 'en_operation', 'medecins', 'appareils']
        


class HopitalSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Hopital
        fields = ['id', 'nom', 'services']


class PatientSerializer(serializers.ModelSerializer):
    # services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'nom', 'tel', 'email', 'message', 'service']