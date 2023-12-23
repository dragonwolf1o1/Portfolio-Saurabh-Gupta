from django.db import models

# Create your models here.

class Contactus(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =   models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    date=models.DateField()
    
    def __str__(self):
        return self.first_name
    
