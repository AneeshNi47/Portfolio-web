from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
     title = models.CharField(max_length=200, default='')
     icon1 = models.ImageField(upload_to='image/', default='')
     icon1link = models.CharField(max_length=200, default='')
     icon2 = models.ImageField(upload_to='image/', default='')
     icon2link = models.CharField(max_length=200, default='')
     icon3 = models.ImageField(upload_to='image/', default='')
     icon3link = models.CharField(max_length=200, default='')
     pub_date = models.DateTimeField()
     body1 = models.TextField(default='',blank=True)
     code1 = models.TextField(default='',blank=True)
     body2 = models.TextField(default='',blank=True)
     code2 = models.TextField(default='',blank=True)
     body3 = models.TextField(default='',blank=True)
     code3 = models.TextField(default='',blank=True)
     image = models.ImageField(upload_to='image/')
     hashtags1 = models.CharField(max_length=200, default='')
     hashtags2 = models.CharField(max_length=200, default='')
     hashtags3 = models.CharField(max_length=200, default='')
     author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

     def __str__(self):
          return self.title

     def summary(self):
          return self.body1[:200]

     def urltitle(self):
          title_url = self.title.replace(" ", "_")
          return title_url
     
     def pub_date_pretty(self):
          return self.pub_date.strftime('%b %e, %Y')
     
     def url_linkedin(self):
          urlinkedin = "http://www.aneeshbharath.com/blog/{}/".format(self.urltitle()) 
          return urlinkedin
     
     def url_fbshrer(self):
          urlfb = "https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fwww.aneeshbharath.com%2Fblog%2F{}%2F&amp;src=sdkpreparse".format(self.urltitle())
          print(self.urltitle())
          return urlfb