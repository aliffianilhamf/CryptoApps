from django.shortcuts import render, redirect
from .forms import CreateUser, Login

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'webapp/index.html')

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