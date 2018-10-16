from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=200)

class Patient(models.Model):
    name = models.CharField(max_length=200)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, related_name="medication", on_delete=models.CASCADE)




