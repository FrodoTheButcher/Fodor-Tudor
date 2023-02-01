from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import TaskDb
from .forms import TaskForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
def main(request):
    return render(request,'main.html')
    

def test(request):
    email = request.GET['email']
    name = request.GET['name']
    password1 = request.GET['password']
    password2 = request.GET['password2']
    return render(request,'test.html',{'email':email
    ,'name':name,'password1':password1,'password2':password2})

def register(request):

    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()   
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created form,fodor e smecher' + user)
                return redirect('login')      
        
        return render(request, 'users/register.html',{'form':form})

def loginpage(request):
     if request.user.is_authenticated:
        return redirect('main')
     else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                messages.info(request,'Udername Or PASSWORD IS INCORECTE')
        context = {}
        return render(request,'users/login.html',context)

def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = TaskDb.objects.all()
            messages.success(request,('New item added'))
            return render(request,'task.html',{'all_items':all_items})

    else:
        all_items = TaskDb.objects.all()
        return render(request,'task.html',{'all_items':all_items})


login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def delete(request,list_id):
    item = TaskDb.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item deleted..'))
    return redirect('task')   

def completed(request,list_id):
    item = TaskDb.objects.get(pk=list_id)
    item.completed=True
    item.save()
    messages.success(request,('Task completed!'))
    return redirect('task')   


