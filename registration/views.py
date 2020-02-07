from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


# Create your views here.
class SignUpView(CreateView):
#configuramos un form_class para indicarle el formulario que debe mostrar que es el UserCreationForm 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#Re defino el metodo get para añadir un "?register" al final de la url despues de registrar un usuario
#y ser redireccionado.
    def get_success_url(self):
            return reverse_lazy('login') + '?register'

#Recupero el formulario por defecto
    def get_form(self, form_class=None):
        #Asigno a la variable la superclase con el get_form.
        form = super(SignUpView, self).get_form()
        # Ahora la voy modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        #form.fields['email'].widget = forms.EmailInput(
            #attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
