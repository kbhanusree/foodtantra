from django.db import models

class accounts(models.Model):
     
     time = models.TimeField()
     date = models.DateField() 
     cuisine = models.CharField(max_length = 50)
     email = models.CharField(max_length=100)
     name = models.CharField(max_length=50)
     people = models.IntegerField() 
   
     