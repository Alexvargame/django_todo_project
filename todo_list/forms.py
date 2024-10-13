from django import forms
from django.forms import widgets

from .models import ToDoItem
class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'cols': 80, 'rows': 20, 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control'}),
        }