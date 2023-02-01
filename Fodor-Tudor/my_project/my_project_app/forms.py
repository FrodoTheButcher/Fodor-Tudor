from django import forms
from .models import TaskDb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskDb
        fields = ['task','priority']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']


