from django.db import models
# Create your models here.

class Tags(models.Model):
    Tag = models.CharField(max_length=50, blank=True, null=True, unique=True) 

    def __str__(self):
        return (self.Tag)


class TO_DO(models.Model):
    Timestamp = models.TimeField(auto_now=True, editable=False)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Tag = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True) 
    Due_Date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, default = 'Open', choices=(
        ('Open','Open'),('Working','Working'),('Done','Done'),('Overdue','Overdue')
        ))
        
    def __str__(self):
        return (self.Title)

