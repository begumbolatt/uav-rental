from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=50)

class Category(models.Model):
    title = models.CharField(max_length=50)   

    def __str__(self):
        return self.title

class UAV(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weigth = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)