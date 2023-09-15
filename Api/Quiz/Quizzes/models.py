from django.db import models
from datetime import datetime

code = (
    ('inactive','inactive'),('active','active'),('finished','finished')
    )


class CreateQuiz(models.Model):
    title = models.CharField(max_length=200)
    Questions = models.CharField(max_length=200)
    Answers = models.IntegerField()
    Start_date = models.TimeField()
    End_date = models.TimeField() 
    status = models.CharField(max_length=20, choices=code)


    def __str__(self):
             return str(self.title)



class Participate(models.Model):
    id = models.AutoField(primary_key=True)
    Write = models.CharField(max_length=100)
   
    def __str__(self):
        return (self.id)
    



       