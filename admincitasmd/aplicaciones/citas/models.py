from django.db import models
from django.db.models.fields import CharField, IntegerField


# Create your models here.

class Citas(models.Model):
    cit_id=models.IntegerField(primary_key=True)
    cit_fecha=models.DateField()
    cit_hora=models.TimeField()
    med_id=models.IntegerField()
    pac_id=models.IntegerField()

class Especialidades(models.Model):
    esp_id=models.IntegerField(primary_key=True)
    esp_nombre=models.CharField(max_length=50)

class Medico(models.Model):
    med_nombre=models.CharField(max_length=50)
    med_apellido=models.CharField(max_length=50)
    med_id=models.IntegerField(primary_key=True)
    esp_id=models.IntegerField()
        
class Paciente(models.Model):
    pac_id=models.IntegerField(primary_key=True)
    pac_nombre=models.CharField(max_length=50)
    pac_apellido=models.CharField(max_length=50)
    pac_ced_ruc=models.CharField(max_length=13)
    pac_cell_telf=models.JSONField()
