
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def AboutPage(request):
    return render(request,'About.html')  

def ContactPage(request):
    return render(request,'contact.html')        

def profile(request):
    if request.user.is_authenticated:
        return render(request,'Profile.html')
    else:
        return redirect('/login/')   

def index1(request):
    if request.method=="POST":
       contact=Contact()
       name=request.POST.get('name')
       email=request.POST.get('email')
       subject=request.POST.get('subject')
       contact.name=name
       contact.email=email
       contact.subject=subject
       contact.save()
       return HttpResponse("<h1> THANK YOU </h1> ")
    return render(request,'index1.html')    

def upload(request):
    return render(request,'index2.html') 

