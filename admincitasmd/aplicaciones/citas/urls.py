
from django.urls import path
from . import views
from aplicaciones.citas.views import crearCitas, citas, medicos, crearMedicos, pacientes, crearPacientes

urlpatterns = [
    path ('', views.home), path('', views.citas),
    path ('citas/', citas,name = 'citas'),
    path ('citas_crear/', crearCitas,name = 'citas_crear'),

    path ('medicos/', medicos,name = 'medicos'),
    path ('medicos_crear/', crearMedicos,name = 'medicos_crear'),
    
    path ('pacientes/', pacientes,name = 'pacientes'),
    path ('pacientes_crear/', crearPacientes,name = 'pacientes_crear'),
]