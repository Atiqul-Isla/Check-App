from django.shortcuts import render, redirect
##Very useful for testing, able to render HttpResponse
from django.http import HttpResponse
from .models import List
from .forms import CreateForm

# Create your views here.
def home(request):
    lists = List.objects.all()
    context = {'lists':lists}
        
    return render(request, 'backend/home.html', context)

def CreateItem(request):
    ##Calling the form that was created by Django in forms.py
    form = CreateForm()
    ##Setting the context which allows us to use our form
    context = {'form':form}
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'backend/create_form.html', context)

def EditItem(request, pk):
    list = List.objects.get(id=pk)
    form = CreateForm(instance=list)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'backend/create_form.html', context)

def DeleteItem(request, pk):
    list = List.objects.get(id=pk)
    # form = CreateForm(instance=list)
    context = {'list':list}
    if request.method == 'POST':
        list.delete()
        return redirect('home')
    return render(request, 'backend/delete_item.html', context)