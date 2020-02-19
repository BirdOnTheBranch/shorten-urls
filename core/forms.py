from django import forms
from .models import Link
from django.forms import ModelForm

    

class UrlForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Aqui tu enlace',})
            }
   
    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        #Elimino el "Este campo es obligatorio que aparece en pantalla"
        for key in self.fields:
            self.fields[key].required = False
            
        #cambio el campo del form que mostraba la label "URL" por defecto en el tamplate.
        #self.fields['url'].label = ""
