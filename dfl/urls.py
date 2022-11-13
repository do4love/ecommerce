from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('main/', views.main, name='main'),
    path('news/', views.news, name='news'),
    path('search/', views.search, name='search'),
    path('single/', views.single, name='single'),
]
