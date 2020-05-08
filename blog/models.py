from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
     title = models.CharField(max_length=200, default='')
     pub_date = models.DateTimeField()
     body1 = models.TextField(default='')
     code1 = models.TextField(default='')
     body2 = models.TextField(default='')
     code2 = models.TextField(default='')
     body3 = models.TextField(default='')
     code3 = models.TextField(default='')
     image = models.ImageField(upload_to='image/')
     hashtags1 = models.CharField(max_length=200, default='')
     hashtags2 = models.CharField(max_length=200, default='')
     hashtags3 = models.CharField(max_length=200, default='')
     author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

     def __str__(self):
          return self.title

     def summary(self):
          return self.body1[:200]
     
     def pub_date_pretty(self):
          return self.pub_date.strftime('%b %e, %Y')
     
     def url_linkedin(self):
          urlinkedin = "https://aneesh-bharath.herokuapp.com/blog/{}/".format(self.id) 
          return urlinkedin
     
     def url_fbshrer(self):
          urlfb = "https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Faneesh-bharath.herokuapp.com%2Fblog%2F{}%2F&amp;src=sdkpreparse".format(self.id) 
          return urlfb