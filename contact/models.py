from django.db import models

# Create your models here.
class Contact(models.Model):
     name = models.CharField(max_length=200, default='name')
     contact_date = models.DateTimeField()
     email = models.CharField(max_length=200, default='email')
     subject = models.CharField(max_length=200, default='subject')
     message = models.CharField(max_length=2000, default='message')
     status = models.CharField(max_length=500, default='Open')
     
     def __str__(self):
          return self.subject