from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if name and password1 and password2:
            a = User(username = name, password=password1)
            a.is_patient = True
            a.save()
            messages.info(request, "user created successfully")
            return redirect('/home/')
        else:
            messages.warning("Check your password well and try again")
    else:
        print("Something went wrong")
    return render(request, 'signup.html')



def home(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        password1 = request.POST['password1']
        if name and password1:
            user = authenticate(request,username = name, password=password1)
            if user.is_active and user is not None:
                login(request, user)
                error = "no"
                if user.is_admin:
                    redirect('/admin_page')
                elif user.is_doctor:
                    return redirect("/doctors_page/")
                elif user.is_patient:
                    return redirect('/patients_page/')
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

