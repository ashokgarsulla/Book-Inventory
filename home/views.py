from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def home(request):
    return render(request, 'home/Index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        print("===================FPRM DATA=======")
        print(username)
        print(first_name)
        print(last_name)
        print(email)
        print(pass1)
        print(pass2)

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

    return render(request, 'home/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print('555555555555555555555555')
        print(user)

        if user is not None:
            login(request,user)
            return redirect('store')


    return render(request,'home/login.html')
