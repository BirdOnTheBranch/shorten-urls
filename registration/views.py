from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import ProfileForm
from django import forms 
from .models import Profile
from core.models import Link


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
            return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
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
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
        
    def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        context['Link'] = Link.objects.filter(usuario=self.request.user) 
        return context