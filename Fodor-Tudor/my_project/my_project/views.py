from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
def base(request):
    return render(request,'main.html')
    

def login(request):
    return render(request,'login.html')

def test(request):
    email = request.GET['email']
    name = request.GET['name']
    password1 = request.GET['password']
    password2 = request.GET['password2']
    return render(request,'test.html',{'email':email
    ,'name':name,'password1':password1,'password2':password2})

def register(request):
    return render(request, 'register.html')