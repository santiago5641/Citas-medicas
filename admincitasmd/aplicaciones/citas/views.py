from django.db.models.fields import IPAddressField
from django.shortcuts import render
from .models import Citas,Paciente,Especialidades,Medico
# Create your views here.

def home(request):
    citas = Citas.objects.all()
    pacientes = Paciente.objects.all()
    epsecialidades = Especialidades.objects.all()
    medico = Medico.objects.all()
    return render(request,"gestioncitas.html", {"citas": citas, })
