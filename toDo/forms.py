from django import forms
from .models import ToDoList


class ToDoChecked(forms.Form):
    completed = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'onClick': 'this.form.submit();'
        }), required=False)
    task = forms.CharField(max_length=40, required=False,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'tasks'
                               }
                           )
                           )


class AddToDoForm(forms.Form):
    task = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'addTask'}))
