from django.db import models
##Importing the general User model provided by Django. Using this we will know what user posts what
from django.contrib.auth.models import User



# Create your models here.
##Created a model of the chat room which sets how our data table looks like and what information it holds
class List(models.Model):
    ##Creating constraints for user, name, description and dates
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField(null=True, blank=True)
    Completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    ##This function ensures the name of the list item is shown as a string and not a data point
    def __str__(self):
        return(self.Name)

    ##Handeling the ordering of how the items are shown
    class Meta:
        ordering = ['-Completed', '-date_updated', '-date_created',] 