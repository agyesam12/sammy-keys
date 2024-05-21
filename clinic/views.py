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

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('/')
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        s = request.POST['specialization']
        try:
            Doctor.objects.create(name=n,mobile=m,specialization=s)
            error="no"
            return redirect('/view_doctors/')
        except:
            error = "yes"
    context = {'error': error}
    return render(request, 'add_doctor.html', context)
    

def view_doctors(request):
    if not request.user.is_staff:
        return redirect('/')
    doc = Doctor.objects.all()
    context = {'doc': doc}
    return render(request, 'view_doctors.html',context)