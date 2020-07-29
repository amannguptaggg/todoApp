from django import forms
from .models import todoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = todoList
        fields = ['title','details']
