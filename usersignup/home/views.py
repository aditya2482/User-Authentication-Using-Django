from email import message
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import UserManager, auth,User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(username = username,password = passw)

        if user is not None:
            login(request,user)
            messages.success(request,'Login Sucessfull')
            return render(request, "index.html",{"Username":username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('index')
    
    return render(request, "login.html")

def signup_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        e_mail = request.POST.get('email')
        password = request.POST.get('password')
        c_password  =request.POST.get('conf_password')
        
        if User.objects.filter(username = u_name):
            message.errors(request,"Username already exist")
            return render(request,'signup_page.html')
        
        if User.objects.filter(email = e_mail):
            message.errors(request,"E_maail already exist")
            return render(request,'signup_page.html')
        
        if password != c_password:
            message.errors(request,"password mismatch")
            return render(request,'signup_page.html')

        myuser = User.objects.create_user(u_name,e_mail,password)
        print("user sucessfully created")
        myuser.save()
        messages.success(request,"Account-Created")
        return render(request,'signup_page.html')

    else:
        return render(request,'signup_page.html')
