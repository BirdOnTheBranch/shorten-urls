from django import forms
from .models import  Profile

class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['avatar', 'notes']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'notes': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'notas'}),
        }
