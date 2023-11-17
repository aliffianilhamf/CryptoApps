from django.shortcuts import render, redirect
from .forms import CreateUser, Login, AddCeritaForm,UpdateCeritaForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from . models import Cerita

# Create your views here.
def index(request):
    cerita = Cerita.objects.all()
    context = {
        'ceritas' : cerita
    }
    return render(request, 'webapp/index.html', context)

# register
def register(request) :
    form = CreateUser()
    
    if request.method == "POST" :
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
           
    context = {
        'form' : form
    }
    return render(request, 'webapp/register.html', context)
        
# login a user
def login(request):
    form = Login()
    if request.method == "POST":
        form = Login(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                
                return redirect("index")
    context = {
        'form' : form
    }
    
    return render(request, 'webapp/login.html', context)

# dashboard
def dashboard(request):
    
    
    return render(request, 'webapp/index.html')


# logout
def logout(request):
    auth.logout(request)
    
    return redirect("login")

# Create
@login_required(login_url='login')
def addCerita(request):
    form = AddCeritaForm()
    
    if request.method == "POST":
        form = AddCeritaForm(request.POST)
        
        if form.is_valid() : 
            form.save() 
            return redirect('index')
    context = {
        'forms' : form
    }
    
    return render(request, 'webapp/addCerita.html', context)
    
    