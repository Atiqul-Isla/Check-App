##Importing ModelForm that makes creating forms much easier for the CRUD functionality
from django.forms import ModelForm 
##Importing our table from models
from .models import List
from django import forms
class CreateForm(ModelForm):
    class Meta:
        ##Identifying what model we want to use
        model = List
        ##Identifying all the fields we want the user to fill in
        fields = '__all__'

        ##Setting widgets to connect django.forms to bootstrap for better styling
        widgets = {
            'User': forms.Select(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your task name here...'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description of your task here...'}),
            'Completed': forms.CheckboxInput(attrs={'class': 'form-control'}),
            
        }

      