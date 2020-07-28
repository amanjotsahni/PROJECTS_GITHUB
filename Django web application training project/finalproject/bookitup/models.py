from django.db import models

class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class book(models.Model):
 First=models.CharField(max_length=100)
 Last=models.CharField(max_length=100)
 Phone=models.BigIntegerField()
 Email=models.CharField(max_length=300)
 Arriving =models.CharField(max_length=100)
 Departure=models.CharField(max_length=100)
 adults=models.BigIntegerField()
 children=models.BigIntegerField()
 questions=models.TextField()

class Login(models.Model):


    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)

class Register(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.CharField(max_length=300)
    upassword=models.CharField(max_length=100)
    ure_password=models.CharField(max_length=100)