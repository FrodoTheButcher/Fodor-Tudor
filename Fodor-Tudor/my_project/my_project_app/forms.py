from django import forms
from .models import TaskDb

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskDb
        fields = ['task','priority']