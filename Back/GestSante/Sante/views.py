from django.shortcuts import redirect, render
from .serializers import HopitalSerializer, PatientSerializer
from .models import Appareil, Hopital, Patient, Service
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PatientCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HopitalView(viewsets.ModelViewSet):
    serializer_class = HopitalSerializer
    queryset = Hopital.objects.all()
    

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    


def mettre_en_operation(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.en_operation = True
    service.save()
    return redirect('admin:Sante_hopital_changelist')  

def mettre_hors_operation(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.en_operation = False
    service.save()
    return redirect('admin:Sante_hopital_changelist')  
    

