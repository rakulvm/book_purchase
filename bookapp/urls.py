from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('login', views.login),
    path('index', views.index, name='index'),
    path('search', views.search),
    path('category', views.category),
    path('checkout', views.checkout),
    path('placeorder', views.placeorder),
]