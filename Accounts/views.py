
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalide details')
            return redirect('login')
    else:
         return render(request,'Login.html')

def Register(request):
    if request.method=="POST":
        firstname=request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"name taken")
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exist")
                return redirect("Register")
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password1,email=email)
                user.save();
                print("User created")


        else:
                print("password not match")

                return redirect("Register")



        return redirect('/')
    else:

         return render(request, 'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')






