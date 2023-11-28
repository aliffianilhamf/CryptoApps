from django.shortcuts import render, redirect,reverse
from .forms import CreateUser, Login, AddCeritaForm,UpdateCeritaForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from . models import Cerita
from django.contrib.auth.models import User 

from django.views import generic,View
from .kripto import orthogonal_encrypt,orthogonal_decrypt
# Create your views here.
def index(request):
    cerita = Cerita.objects.all().order_by('-id')
    username = request.user.username
    if not username == 'aliffianilham' : 
        uss = orthogonal_decrypt(username,6)
    else :
        uss = username
     
    dekrip_cerita = []
    for i,crt in enumerate(cerita, start=1):
        dekrip_judul = orthogonal_decrypt(crt.judul,6)
        dekrip_konten = orthogonal_decrypt(crt.konten,6)
        id = crt.id
        dekrip_cerita.append({
            'judul': dekrip_judul,
            'konten' : dekrip_konten,
            'id' : id,
            "ceritas" :cerita
        })
   
    context = {
        'ceritas' : dekrip_cerita,
        'uss' : uss
    }
    return render(request, 'webapp/index.html', context)

# register
def register(request) :
    form = CreateUser()
    
    if request.method == "POST" :
        request.POST._mutable = True
        request.POST['username'] = orthogonal_encrypt(request.POST['username'],6)
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
        if request.POST['username'] != 'aliffianilham' :
            request.POST._mutable = True
            request.POST['username'] = orthogonal_encrypt(request.POST['username'],6)
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
        request.POST['judul'] = orthogonal_encrypt(request.POST['judul'],6)
        request.POST['konten'] = orthogonal_encrypt(request.POST['konten'],6)
        form = AddCeritaForm(request.POST, request.FILES)
        if form.is_valid() : 
            form.save()
           
            return redirect('index')
    context = {
        'forms' : form
    }
    
    return render(request, 'webapp/addCerita.html', context)

#detail cerita
def detail(request, pk) :
    cerita = Cerita.objects.get(id = pk)
    dekrip_cerita=[]
    cerita_id = cerita.id
    dekrip_judul = orthogonal_decrypt(cerita.judul,6)
    dekrip_konten = orthogonal_decrypt(cerita.konten,6)
    
    print(dekrip_judul)
    dekrip_cerita.append({
        'judul' : dekrip_judul,
        'konten' : dekrip_konten,
        'id' :cerita_id,
        "cerita" :cerita
        
    })
    context = {
        'cerita' : dekrip_cerita
    }
    return render(request, 'webapp/detailCerita.html', context)