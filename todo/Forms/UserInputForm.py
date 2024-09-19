from django import forms
from todo.Models.models import ToDoItem

class UserInputForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['text', 'due_date']

    widgets = {
        'due_date' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    }
