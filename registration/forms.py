from django import forms
from django.forms import BaseModelFormSet
from .models import  Profile
from core.models import Link

class UrlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Copia aqui tu enlace',})
            }
   
    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        #Elimino el "Este campo es obligatorio que aparece en pantalla"
        for key in self.fields:
            self.fields[key].required = False
        #cambio el campo del form que mostraba la label "URL" por defecto en el tamplate.
        self.fields['url'].label = ""


class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['avatar', 'notes', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'notes': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'notas'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }


