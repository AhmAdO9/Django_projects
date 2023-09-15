from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    Username = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Category = models.CharField(max_length=30)
    Dp = models.ImageField(null=True, blank=True)
    Speciality = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.Username
    

class Blog(models.Model):
    Title = models.CharField(max_length=60)
    Image = models.ImageField(null=True, blank=True)
    Categories = models.CharField(max_length=30, null=True, blank=True)
    Summary = models.CharField(max_length=2000, null=True, blank=True)
    Content = models.CharField(max_length=10000,null=True, blank=True)
    Written_by = models.CharField(max_length=30, null=True, blank=True, default=True)

    def __str__(self):
        return self.Title
    
class Draft(models.Model):
    Title = models.CharField(max_length=60)
    Image = models.ImageField(null=True, blank=True)
    Categories = models.CharField(max_length=30, null=True, blank=True)
    Summary = models.CharField(max_length=2000, null=True, blank=True)
    Content = models.CharField(max_length=10000,null=True, blank=True)
    Written_by = models.CharField(max_length=30, null=True, blank=True, default=True)


    def __str__(self):
        return self.Title
    
class Appointment(models.Model):
    Speciality = models.CharField(max_length=60,null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.date_time
