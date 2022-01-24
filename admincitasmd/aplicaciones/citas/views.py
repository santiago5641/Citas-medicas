from django import forms
from django.shortcuts import redirect, render

from .forms import formcitas, formmedicos, formpacientes
#from django.contrib.auth.forms import UserCreationForm
from .models import Citas,Paciente,Especialidades,Medico
from django.contrib import messages

import logging as log
# Create your views here.

def home(request):
    citas = Citas.objects.all()
    pacientes = Paciente.objects.all()
    especialidades = Especialidades.objects.all()
    medico = Medico.objects.all()
    # return render(request,"gestioncitas.html", {"citas": citas, "pacientes": pacientes, "especialidades": especialidades, "medico": medico})
    return render(request,"index.html", {"citas": citas, "pacientes": pacientes, "especialidades": especialidades, "medico": medico})

def gestion(request):
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
            
            messages.success(request,"creado correctamente")

        else:
            print("no valido")

        
    return render (request, 'citas/citas_crear.html', {'form': form})

    # eliminar citas
def eliminarCitas(request, cit_id):    
    citas= Citas.objects.get(cit_id=cit_id)
    citas.delete()
    messages.success(request,"eliminado correctamente")
    return redirect('/citas')

def editarCitas(request,cit_id):

    citas= Citas.objects.get(cit_id=cit_id)
    print(citas.cit_hora)
    cit_fecha= citas.cit_fecha
    cit_hora= citas.cit_hora
    med_id= citas.med_id
    pac_id=citas.pac_id
  
    form= formcitas(initial={'cit_fecha':cit_fecha,'cit_hora':cit_hora,'med_id':med_id, 'pac_id':pac_id})
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
            messages.success(request,"editado correctamente")
        else:
            print("no valido")

        
    return render (request, 'citas/citas_editar.html', {'form': form})




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
            medicos.esp_id= form.cleaned_data['esp_id']

            medicos.save()
            messages.success(request,"creado correctamente")
        else:
            print("no valido")

        
    return render (request, 'medicos/medicos_crear.html', {'form': form})

def eliminarMedicos(request, med_id):    
        medicos= Medico.objects.get(med_id=med_id)
        medicos.delete()
        messages.success(request,"creado correctamente")
        return redirect('/medicos')


def editarMedicos(request,med_id):
    medicos= Medico.objects.get(med_id=med_id)
    med_nombre=medicos.med_nombre
    med_apellido= medicos.med_apellido
    esp_id=medicos.esp_id
    form= formmedicos(initial={'med_nombre':med_nombre,'med_apellido':med_apellido,'esp_id':esp_id})
    if request.method == "POST":
        print(request.POST)
        form= formmedicos(request.POST)

        if form.is_valid():
            print("valido")
            medicos = Medico()
            medicos.med_nombre= form.cleaned_data['med_nombre']
            medicos.med_apellido= form.cleaned_data['med_apellido']
            medicos.esp_id= form.cleaned_data['esp_id']

            medicos.save()
            messages.success(request,"creado correctamente")
        else:
            print("no valido")

        
    return render (request, 'medicos/medicos_crear.html', {'form': form})


# listado y crear paciente
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

            pacientes.save()

            messages.success(request,"creado correctamente")

        else:
            print("no valido")

        
    return render (request, 'pacientes/pacientes_crear.html', {'form': form})

def eliminarPacientes(request, pac_id):    
        pacientes= Paciente.objects.get(pac_id=pac_id)
        pacientes.delete()
        messages.success(request,"creado correctamente")
        return redirect('/pacientes')

def editarPacientes(request,pac_id):
    pacientes= Paciente.objects.get(pac_id=pac_id)
    pac_nombre=pacientes.pac_nombre
    pac_apellido= pacientes.pac_apellido
    pac_ced_ruc= pacientes.pac_ced_ruc
    pac_cell_telf= pacientes.pac_cell_telf
    form= formpacientes(initial={'pac_nombre':pac_nombre,'pac_apellido':pac_apellido,'pac_ced_ruc':pac_ced_ruc,'pac_cell_telf':pac_cell_telf})
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
            
            
            pacientes.save()    
            messages.success(request,"creado correctamente")
        else:
            print("no valido")

        
    return render (request, 'pacientes/pacientes_crear.html', {'form': form})

