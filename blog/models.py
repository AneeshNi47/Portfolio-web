from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
     title = models.CharField(max_length=200, default='')
     pub_date = models.DateTimeField()
     body = models.TextField()
     image = models.ImageField(upload_to='image/')
     #title = models.ForeignKey('Subject', default=1, on_delete=models.CASCADE)
     hashtags1 = models.CharField(max_length=200, default='')
     hashtags2 = models.CharField(max_length=200, default='')
     hashtags3 = models.CharField(max_length=200, default='')
     #author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

     def __str__(self):
          return self.title

     def summary(self):
          return self.body[:200]
     
     def pub_date_pretty(self):
          return self.pub_date.strftime('%b %e %Y')

class Subject(models.Model):
     stitle = models.CharField(max_length=200, default='null')
     create_date = models.DateTimeField()

     def __str__(self):
          return self.stitle