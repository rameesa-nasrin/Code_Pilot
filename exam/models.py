from django.db import models

from accounts.models import User

from datetime import datetime,time,timedelta

# Create your models here.

class Assessment(models.Model):

    LANGUAGE_CHOICES = {
        ("python","python"),
        ("java","java"),
        ("c","c"),
        ("c++","c++"),
        ("other","other")
    }

    STATUS_CHOICES = {
        ("scheduled","scheduled"), 
        ("pending","pending"),
        ("in progress","in progress"),
        ("completed","completed")
    }

    title = models.CharField(max_length=100)

    batch = models.CharField(max_length=100)

    language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES)

    exam_date = models.DateField()

    duration = models.PositiveIntegerField()

    start_time = models.TimeField()

    end_time = models.TimeField(null=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="scheduled")

    
    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):

        end_date_time = datetime.combine(self.exam_date,self.start_time)+timedelta(hours=self.duration)

        self.end_time = end_date_time.time()

        return super().save(*args,**kwargs)