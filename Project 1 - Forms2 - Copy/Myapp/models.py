from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.TextField()
    company = models.TextField()
    last_date=models.DateField()
    
    def __str__(self):#The object of the person(Person1(object),Person2(object)is converted into a string)
        return self.job_name