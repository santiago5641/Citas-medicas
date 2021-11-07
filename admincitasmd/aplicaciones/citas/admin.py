from django.contrib import admin
from .models import Citas
from .models import Especialidades
from .models import Medico
from .models import Paciente

# Register your models here.
admin.site.register(Citas)
admin.site.register(Especialidades)
admin.site.register(Medico)
admin.site.register(Paciente)
