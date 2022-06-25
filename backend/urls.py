from django.urls import path
##Importing the filler function from views.py file
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('create-item', views.CreateItem, name='create-item'),
    path('edit-item/<str:pk>/', views.EditItem, name='edit-item'),
    path('delete-item/<str:pk>/', views.DeleteItem, name='delete-item')
]
