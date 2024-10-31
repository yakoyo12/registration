from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def signuppage(request):
    if request.method== 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        
        if pass1 != pass2:
            return HttpResponse('your password and comfirm password is not the same')
        else:

            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            
        
    


def loginpage(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        email = authenticate(request, email=email, password=password)
        if email is not None:
            login(request,email)
            return redirect('home')
        else:
            return HttpResponse('Email or Password is incorrect!! ')


    return render(request, 'login.html')