from django.db import models

# Create your models here.

class Job(models.Model):
     title = models.CharField(max_length=200, default='Title')
     image = models.ImageField(upload_to='image/')
     summary = models.CharField(max_length=200, default='summary')
     job_url = models.URLField(max_length=200, default='SOME STRING')


class Vistor(models.Model):
     userip = models.CharField(max_length=200)
     location = models.CharField(max_length=200, default='None')
     visit_date = models.DateTimeField(blank=True)