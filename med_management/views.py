from django.shortcuts import render
from .models import Patient, Medication, Prescription

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PatientSerializer, MedicationSerializer,PrescriptionSerializer

def index(request):
    return HttpResponse("Wellframe Tech Challenge")

class PatientViewSet(viewsets.ModelViewSet):
    """
    get:
    Return a list of all patients

    post:
    Create a new patient
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):

    """
    get:
    Return a list of all prescriptions

    post:
    Create a new prescription
    """
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    """
    get:
    Return a list of all medications

    post:
    Create a new medication
    """
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer