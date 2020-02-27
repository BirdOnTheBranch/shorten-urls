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
        super().__init__(*args, **kwargs)
        #del "This field is required" on template.
        for key in self.fields:
            self.fields[key].required = False
