from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import book_table
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        db_list = book_table.objects.all()
        for db1 in db_list:
            if db1.username == username:
                return HttpResponse("Username not available! Enter another username..")
        if password == cpassword:
            booktable = book_table(name=name, username=username, password=password)
            booktable.save()
            flag=True
            return render(request, 'login.html')
        else:
            return HttpResponse("Passwords does not match")
    return render(request, 'register.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    db_list = book_table.objects.all()
    for db in db_list:
        print(db.username)
        if db.username == username and db.password == password:
            return render(request, 'index.html')
    return render(request, 'login.html')