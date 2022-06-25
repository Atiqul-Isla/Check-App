##Importing ModelForm that makes creating forms much easier for the CRUD functionality
from django.forms import ModelForm 
##Importing our table from models
from .models import List

class CreateForm(ModelForm):
    class Meta:
        ##Identifying what model we want to use
        model = List
        ##Identifying all the fields we want the user to fill in
        fields = '__all__'

