from django.shortcuts import render, redirect, get_object_or_404   
from django.contrib.auth.models import User 
from .models import Link
from .forms import UrlForm
from .shortner import Shortner


# Create your views here.
#le paso la variable <str:code> que declaro en path de urls.py
def RedirectView(request, code):
#le paso el modelo y filtro el resultado por code
    link = get_object_or_404(Link, code=code)
    return redirect(link.url)

        
def HomeView(request):
    form = UrlForm(request.POST)
    code = ""
    link = ""
    if request.user.is_authenticated:
        link = Link.objects.filter(usuario=request.user)
    if request.method == "POST":
        #comprueba si el formulario es valido y si el campo "url" del formulario no es None
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
    