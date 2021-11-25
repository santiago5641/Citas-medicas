from django.db import models
from django.db.models.fields import CharField, IntegerField


# Create your models here.


class Especialidades(models.Model):
    esp_id=models.IntegerField(primary_key=True)
    esp_nombre=models.CharField(max_length=50)

    def  __str__(self):
        texto="{0} "
        return texto.format (self.esp_nombre)


class Paciente(models.Model):
    pac_id=models.IntegerField(primary_key=True)
    pac_nombre=models.CharField(max_length=50)
    pac_apellido=models.CharField(max_length=50)
    pac_ced_ruc=models.CharField(max_length=13)
    pac_cell_telf=models.JSONField()

    def  __str__(self):
        texto="{0} {1} "
        return texto.format (self.pac_nombre, self.pac_apellido)

class Medico(models.Model):
    med_nombre=models.CharField(max_length=50)
    med_apellido=models.CharField(max_length=50)
    med_id=models.IntegerField(primary_key=True)
    esp_id=models.ForeignKey(Especialidades, on_delete=models.CASCADE)

    def  __str__(self):
        texto="{0} {1} ({2})"
        return texto.format (self.med_nombre, self.med_apellido, self.esp_id)
        
class Citas(models.Model):
    cit_id=models.IntegerField(primary_key=True)
    cit_fecha=models.DateField()
    cit_hora=models.TimeField()
    med_id=models.ForeignKey(Medico, on_delete=models.CASCADE)
    pac_id=models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def  __str__(self):
        texto="{0} {1} {2} {3} {4}"
        return texto.format (self.cit_id, self.cit_fecha, self.cit_hora, self.med_id, self.pac_id)