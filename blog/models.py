from django.db import models

# Create your models here.





class Courses(models.Model):
    title = models.CharField(max_length=200,blank=False)
    thumbnail = models.ImageField()
    overview = models.CharField(max_length=1000, blank=True)