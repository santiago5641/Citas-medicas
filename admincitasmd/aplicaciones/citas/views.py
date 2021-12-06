from django import forms
from django.shortcuts import redirect, render

from .forms import formcitas, Citasform, formmedicos, formpacientes
#from django.contrib.auth.forms import UserCreationForm
from .models import Citas,Paciente,Especialidades,Medico

import logging as log
# Create your views here.

def home(request):
    citas = Citas.objects.all()
    pacientes = Paciente.objects.all()
    especialidades = Especialidades.objects.all()
    medico = Medico.objects.all()
    return render(request,"gestioncitas.html", {"citas": citas, "pacientes": pacientes, "especialidades": especialidades, "medico": medico})


# GESTION CITAS 
#citas es lita de citas
def citas(request):
    citas = Citas.objects.all()
    return render(request, "citas/citaslistado.html", {"citas": citas})

# def registrarcitas(request):
#     cit_fecha= request.POST['cit_fecha']
#     cit_hora= request.POST['cit_hora']
#     med_id= request.POST['id_med_id']
#     pac_id= request.POST['id_pac_id']
#     log.info(cit_hora)

#     cita = Citas.objects.create(cit_fecha=cit_fecha, cit_hora=cit_hora, med_id=med_id, pac_id=pac_id)
#     return redirect('../citas')

# crear citas 
def crearCitas(request):
    form= formcitas()
    if request.method == "POST":
        print(request.POST)
        form= formcitas(request.POST)

        if form.is_valid():
            print("valido")
            citas = Citas()
            citas.cit_fecha= form.cleaned_data['cit_fecha']
            citas.cit_hora= form.cleaned_data['cit_hora']
            citas.med_id= form.cleaned_data['med_id']
            citas.pac_id= form.cleaned_data['pac_id']

            citas.save()

        else:
            print("no valido")

        
    return render (request, 'citas/citas_crear.html', {'form': form})

   #creacion de medicos  
def medicos(request):
    medicos = Medico.objects.all()
    
    return render(request, "medicos/medicoslistados.html", {"medicos": medicos})

def crearMedicos(request):
    form= formmedicos()
    if request.method == "POST":
        print(request.POST)
        form= formmedicos(request.POST)

        if form.is_valid():
            print("valido")
            medicos = Medico()
            medicos.med_nombre= form.cleaned_data['med_nombre']
            medicos.med_apellido= form.cleaned_data['med_apellido']
            medicos.pac_id= form.cleaned_data['pac_id']

            medicos.save()

        else:
            print("no valido")

        
    return render (request, 'medicos/medicos_crear.html', {'form': form})

def pacientes(request):
    pacientes = Paciente.objects.all()
    
    return render(request, "pacientes/pacienteslistado.html", {"pacientes": pacientes})

def crearPacientes(request):
    form= formpacientes()
    if request.method == "POST":
        print(request.POST)
        form= formpacientes(request.POST)

        if form.is_valid():
            print("valido")
            pacientes = Paciente()
            pacientes.pac_nombre= form.cleaned_data['pac_nombre']
            pacientes.pac_apellido= form.cleaned_data['pac_apellido']
            pacientes.pac_ced_ruc=form.cleaned_data['pac_ced_ruc']
            pacientes.pac_cell_telf=form.cleaned_data['pac_cell_telf']

            medicos.save()

        else:
            print("no valido")

        
    return render (request, 'pacientes/pacientes_crear.html', {'form': form})