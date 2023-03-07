from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpRequest

from app.forms import UAVForm
from . import models
from django.contrib.auth import login

# Create your views here.

def home_page(request):
    context  = {'context': models.UAV.objects.all()}
    print(context)
    return render(request, 'app/index.html', context ) 

#authentication views

def register_page(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        surname = request.POST.get('surname', False)
        email = request.POST.get('email', False)
        phone = request.POST.get('phone', False)
        password = request.POST.get('password', False)

        if models.User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return render(request, "app/authentication/register.html")
        else:
            user = models.User(name=name, surname=surname, email=email, phone=phone, password=password)
            user.save()

        return redirect('/')
    else : 
        return render(request, "app/authentication/register.html")


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        users = models.User.objects.values_list('email', 'password')
        user = users.filter(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/", {user})
        else:
            return render(request, "app/authentication/login.html")
    return render(request, "app/authentication/login.html")

def uav_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = UAVForm()
        else:
            uav = models.UAV.objects.get(pk=id)
            form = UAVForm(instance=uav)
        return render(request, "app/uav/uav_form.html", {'form': form})
    else:
        if id==0:
            form = UAVForm(request.POST)
        else:
            uav = models.UAV.objects.get(pk=id)
            form = UAVForm(request.POST, instance=uav)
        if form.is_valid():
            form.save()
        return redirect('/')

def uav_delete(request,id):
    uav = models.UAV.objects.get(pk=id)
    uav.delete()
    return redirect('/')



