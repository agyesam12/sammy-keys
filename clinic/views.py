from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def home(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        password1 = request.POST['password1']
        if name and password1:
            user = authenticate(request,username = name, password=password1)
            if user.is_staff:
                login(request, user)
                error = "no"
                redirect('/admin_page')
            else:
                return redirect('/')
                error = "yes"
        else:
            print ("Something went wrong")
    context = {'error':error}
    return render(request, 'home.html',context)



def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def admin_page(request):
    if not request.user.is_staff:
        return redirect('/')
    return render(request, 'admin_page.html')

def signout(request):
    if not request.user.is_staff:
        redirect('/about/')
    logout(request)
    return redirect('/')

