
from django.urls import path
from django.urls.resolvers import _PATH_PARAMETER_COMPONENT_RE
from . import views
from aplicaciones.citas.views import crearCitas, citas, medicos, crearMedicos, pacientes, crearPacientes,eliminarCitas,eliminarMedicos,eliminarPacientes, editarCitas, editarMedicos, editarPacientes

urlpatterns = [
    # crear rutas de citas
    path ('', views.home), path('', views.citas),
    path ('citas/', citas,name = 'citas'),
    path ('citas_crear/', crearCitas,name = 'citas_crear'),
    path ('citas_eliminar/<int:cit_id>', eliminarCitas,name = 'citas_eliminar'),
    path ('citas_editar/<int:cit_id>', editarCitas,name ='citas_editar'),
    

    # crear rutas de medicos
    path ('medicos/', medicos,name = 'medicos'),
    path ('medicos_crear/', crearMedicos,name = 'medicos_crear'),
    path ('medicos_eliminar/<int:med_id>', eliminarMedicos,name = 'medicos_eliminar'),
    path ('medicos_editar/<int:med_id>', editarMedicos,name ='medicos_editar'),

    # crear rutas pacientes 
    path ('pacientes/', pacientes,name = 'pacientes'),
    path ('pacientes_crear/', crearPacientes,name = 'pacientes_crear'),
    path ('pacientes_eliminar/<int:pac_id>', eliminarPacientes,name = 'pacientes_eliminar'),
    path ('pacientes_editar/<int:med_id>', editarPacientes,name ='pacientes_editar'),
    

    
]