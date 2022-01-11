from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import VacunaFormulario, UserRegisterForm
from AppCoder.models import Vacunas, Barbijos, Oximetros
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#Render del inicio


def inicio(request):
    return render(request, "AppCoder/inicio.html")

#Render de acerca de mi
def acerca_de_mi(request):
    return render(request, "AppCoder/acerca_de_mi.html")

#Render de todas las clases

def barbijos(request):
    return render(request,"AppCoder/barbijos.html")

def oximetros(request):
    return render(request,"AppCoder/oximetros.html")

def vacunas(request):
    return render(request, "AppCoder/vacunas.html")

#CRUD Vacunas

class VacunaList(ListView):
    model = Vacunas
    template_name = 'AppCoder/vacuna_list.html'

class VacunaDetalle(LoginRequiredMixin, DetailView):
    model = Vacunas
    template_name = 'AppCoder/vacuna_detalle.html'
    
class VacunaCreacion(LoginRequiredMixin,CreateView):
    
    model = Vacunas
    success_url = "/AppCoder/vacuna/list"
    fields = ['proveedor', 'fecha_creacion', 'pais_origen', 'grado_de_dolor']

class VacunaUpdate(LoginRequiredMixin, UpdateView):
    
    model = Vacunas
    success_url = "/AppCoder/vacuna/list"
    fields = ['proveedor', 'fecha_creacion', 'pais_origen', 'grado_de_dolor']

class VacunaDelete(LoginRequiredMixin, DeleteView):
    
    model = Vacunas
    success_url = "/AppCoder/vacuna/list"
 
def vacunaFormulario(request):
    if request.method == 'POST':
        miFormulario = VacunaFormulario(request.POST)        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            abc = Vacunas(proveedor=informacion['proveedor'],fecha_creacion=informacion['fecha_creacion'],pais_origen=informacion['pais_origen'],grado_de_dolor=informacion['grado_de_dolor'])
            abc.save()
            return render(request,"AppCoder/inicio.html")
    else:
        
        miFormulario = VacunaFormulario()
        
    return render(request,"AppCoder/vacunaFormulario.html", {"miFormulario": miFormulario})

def eliminarVacunas(request, vacuna_proveedor):
    
    vacuna_borrada = Vacunas.objects.get(proveedor=vacuna_proveedor)
    vacuna_borrada.delete()
    vacunas = Vacunas.objects.all
    contexto = {'vacunas':vacunas}  
    return render(request, "AppCoder/leerVacunas.html", contexto)

#CRUD Barbijos

class BarbijosList(ListView):
    model = Barbijos
    template_name = 'AppCoder/barbijo_list.html'

class BarbijosDetalle(LoginRequiredMixin, DetailView):
    model = Barbijos
    template_name = 'AppCoder/barbijo_detalle.html'
    
class BarbijosCreacion(LoginRequiredMixin,CreateView):
    
    model = Barbijos
    success_url = "/AppCoder/barbijo/list"
    fields = ['marca', 'tamanio', 'precio']

class BarbijosUpdate(LoginRequiredMixin, UpdateView):
    
    model = Barbijos
    success_url = "/AppCoder/barbijo/list"
    fields = ['marca', 'tamanio', 'precio']

class BarbijosDelete(LoginRequiredMixin, DeleteView):
    
    model = Barbijos
    success_url = "/AppCoder/barbijo/list"
 

#CRUD Oximetro

class OximetrosList(ListView):
    model = Oximetros
    template_name = 'AppCoder/oximetro_list.html'

class OximetrosDetalle(LoginRequiredMixin, DetailView):
    model = Oximetros
    template_name = 'AppCoder/oximetro_detalle.html'
    
class OximetrosCreacion(LoginRequiredMixin,CreateView):
    
    model = Oximetros
    success_url = "/AppCoder/oximetro/list"
    fields = ['marca', 'modelo', 'precio']

class OximetrosUpdate(LoginRequiredMixin, UpdateView):
    
    model = Oximetros
    success_url = "/AppCoder/oximetro/list"
    fields = ['marca', 'modelo', 'precio']

class OximetrosDelete(LoginRequiredMixin, DeleteView):
    
    model = Oximetros
    success_url = "/AppCoder/oximetro/list"
 
#login/logout

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario =form.cleaned_data.get('username')
            contra =form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                
                login(request,user)            
                
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido {usuario}"} )
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Error datos incorrectos"} )
        else:
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Error datos incorrectos"} )
    form = AuthenticationForm()
    
    return render(request, "AppCoder/login.html", {'form': form})


def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            
            form.save()
            
            return render(request, "AppCoder/inicio.html", {"mensaje":"{username} creado"})
    else:
        
        form = UserRegisterForm()
    
    return render(request, "AppCoder/register.html", {"form": form})                       


