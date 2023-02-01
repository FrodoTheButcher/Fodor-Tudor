"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path("",views.main, name='main'),
    path("test/",views.test,name='test'),
    path("register/", views.register, name='register'),
    path("task/", views.task, name='task'),
    path("delete/<list_id>", views.delete, name='delete'),
    path("completed/<list_id>", views.completed, name='completed'),
    path("login/",LoginView.as_view(), name='login'),
    path("logout/",LogoutView.as_view(), name='logout'),

]
