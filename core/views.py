from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib.auth.models import User
from django.urls import reverse
from core import views
from .models import Link
from .forms import UrlForm
from .shortner import Shortner



# Create your views here.
def RedirectView(request, code):
    """ Redirect to url"""
    link = get_object_or_404(Link, code=code)   
    return redirect(link.url)
        
        
def HomeView(request):
    """ Create code and render in template whith forms and urls of request.user"""
    form = UrlForm(request.POST)
    code = ""
    link = ""
    if request.user.is_authenticated:
        link = Link.objects.filter(usuario=request.user )
    if request.method == "POST":
        if form.is_valid() and form.data['url']: 
            NewUrl = form.save(commit=False)
            code = Shortner().issue_token()
            NewUrl.code = code
            if isinstance(request.user, User):
                NewUrl.usuario = request.user
            NewUrl.save()
        else:
            form = UrlForm()
            code = "Invalid URL"

    return render(request, 'core/home.html', {'form':form, 'code':code, 'link':link })
