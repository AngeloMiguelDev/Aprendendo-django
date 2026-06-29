from django.urls import path
from . import views

urlpatterns = [
    path('ver/', views.ver_home, name ="ver_home"),
    path('produto', views.produto, name= "produto")
]