from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import register_user, book_details
from .forms import register_form, login_form
from django.core.paginator import Paginator, EmptyPage

def home(request):
    return render(request, "home.html")

def register(request):
    ''' Get details from register page and save in user_details '''
    form = register_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST['name']
            username = request.POST['username']
            password = request.POST['password']
            repassword = request.POST['repassword']
            pwd = make_password(password)
            save_user = register_user(name=name, username=username, password=pwd)
            save_user.save()
            return render(request, 'login.html')
    return render(request, 'register.html', {'form': form})

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
    form = login_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return redirect('index')
    return render(request, 'login.html', {'form': form})

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

def checkout(request):
    return render(request, 'checkout.html')

def placeorder(request):
    return render(request, 'placeorder.html')