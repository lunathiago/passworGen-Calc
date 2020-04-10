from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('geraSenha/', views.geraSenha, name="geraSenha"),
    path('calculate/', views.calculate, name="calculate"),
    path('madeby/', views.madeby, name="madeby"),
]
