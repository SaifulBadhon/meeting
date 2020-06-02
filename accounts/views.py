from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("/profile")

    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/profile")
        else:
            messages.info(request,"invalid credential")
            return redirect("/")

        

    else:
        return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(first+last)

        if pass1==pass2:
            user = User.objects.create_user(username = first+last, email = email, password = pass1 )
            user.save
            return redirect("/")
        else:
            messages.info(request,"password doesn't match")
            return redirect("/register")
    else:        
        return render(request,"register.html")


def profile(request):
    return render(request,"profile.html")

def logout(request):
    auth.logout(request)
    return redirect("/")