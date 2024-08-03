from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    status=models.IntegerField()

    image = models.ImageField(upload_to="Profile", blank=True, null=True)

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
       return self.name   
