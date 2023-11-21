from django.shortcuts import render, redirect
from .forms import CreateUser, Login, AddCeritaForm,UpdateCeritaForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from . models import Cerita
from django.contrib.auth.models import User 

from django.views import generic,View
from .kripto import enkripsi_caesar,dekripsi_caesar
# Create your views here.
def index(request):
    cerita = Cerita.objects.all().order_by('-id')
    # if request.user.is_authenticated:
    #     user = dekripsi_caesar(request.user.username, 3)
    # else:
    #     user = None 
        
    dekrip_cerita = []
    for i,crt in enumerate(cerita, start=1):
        dekrip_judul = dekripsi_caesar(crt.judul,3)
        dekrip_konten = dekripsi_caesar(crt.konten,3)
        penulis_id = str(crt.penulis.id)
        usr = User.objects.get(id=penulis_id)
        dekrip_penulis = dekripsi_caesar(usr.username,3)
        dekrip_cerita.append({
            'judul': dekrip_judul,
            'konten' : dekrip_konten,
            #'image': dekrip_image,
            'penulis' : dekrip_penulis,
            "ceritas" :cerita
        })
    context = {
        'ceritas' : dekrip_cerita,
        #'user' : user
    }
    return render(request, 'webapp/index.html', context)

# register
def register(request) :
    form = CreateUser()
    
    if request.method == "POST" :
        request.POST._mutable = True
        request.POST['username'] = enkripsi_caesar(request.POST['username'],3)
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
        request.POST._mutable = True
        request.POST['username'] = enkripsi_caesar(request.POST['username'],3)
        form = Login(request, data=request.POST)
        if form.is_valid():
            #request.POST._mutable = True
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
        request.POST._mutable = True
        request.POST['judul'] = enkripsi_caesar(request.POST['judul'],3)
        request.POST['konten'] = enkripsi_caesar(request.POST['konten'],3)
       # request.POST['image'] = enkripsi_caesar(request.POST['image'],3)
        #print(request.POST['penulis'])
        #request.POST['penulis'] = enkripsi_caesar(request.POST['penulis'],3)
        form = AddCeritaForm(request.POST, request.FILES)
        if form.is_valid() : 
            form.save()
           
            return redirect('index')
    context = {
        'forms' : form
    }
    
    return render(request, 'webapp/addCerita.html', context)

    
    