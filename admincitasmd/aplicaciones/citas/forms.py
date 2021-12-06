
from django import forms

from .models  import Citas, Especialidades, Medico, Paciente

class Citasform(forms.ModelForm):
    class Meta:
        model = Citas
        fields= '__all__'

class formcitas(forms.Form):
    
    cit_fecha=forms.DateField(required=True, widget=forms.DateInput)
    cit_hora=forms.TimeField(required=True, widget=forms.DateInput)
    med_id=forms.ModelChoiceField(queryset=Medico.objects.all())
    pac_id=forms.ModelChoiceField(queryset=Paciente.objects.all())


class formmedicos(forms.Form):
    
    med_nombre=forms.CharField(required=True, widget=forms.DateInput)
    ned_apellido=forms.CharField(required=True, widget=forms.DateInput)
    esp_id=forms.ModelChoiceField(queryset=Especialidades.objects.all())

class formpacientes(forms.Form):
    
    pac_nombre=forms.CharField(required=True, widget=forms.DateInput)
    pac_apellido=forms.CharField(required=True, widget=forms.DateInput)
    pac_ced_ruc=forms.CharField(required=True, widget=forms.DateInput)
    pac_cell_telf=forms.JSONField(required=True, widget=forms.DateInput)
    med_id=forms.ModelChoiceField(queryset=Especialidades.objects.all())