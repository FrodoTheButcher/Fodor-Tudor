from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import TaskDb
from .forms import TaskForm
from django.contrib import messages
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
    return render(request, 'register.html')

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


