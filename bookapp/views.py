from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import book_table, book_details
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage

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

def index(request):
    books = book_details.objects.all().order_by('name')
    p = Paginator(books, 4)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'index.html', {'books': page})

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    db_list = book_table.objects.all()
    for db in db_list:
        print(db.username)
        if db.username == username and db.password == password:
            return redirect('index')

    return render(request, 'login.html')

def search(request):
    book_name = request.GET.get('book_name')
    status = book_details.objects.filter(name__startswith=book_name)
    if status:
        return render(request, 'search_books.html', {'books':status})
    else:
        return HttpResponse("Book not found!")

def category(request):
    category1 = request.GET.get('dropdown1')
    status = book_details.objects.filter(category__startswith=category1)
    if status:
        return render(request, 'search_books.html', {'books':status})
    else:
        return HttpResponse("Book not found!")