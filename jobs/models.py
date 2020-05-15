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


class JobImage(models.Model):
     blog_id = models.ForeignKey(Job, on_delete=models.CASCADE, default=1)
     img_label= models.CharField(max_length=200, default='Title')
     image = models.ImageField(upload_to='image/')
     alt_description = models.CharField(max_length=200, default='')
     img_description = models.CharField(max_length=200, default='')


class Services(models.Model):
     service_title = models.CharField(max_length=200, default='')
     service_icon = models.ImageField(upload_to='image/')
     service_description = models.CharField(max_length=200, default='')

     def __str__(self):
          return self.service_title
     

class ServicePoints(models.Model):
     service_id = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
     service_point = models.CharField(max_length=200, default='')
     
     def __str__(self):
          return self.service_point


class Testimonial(models.Model):
     image = models.ImageField(upload_to='image/')
     comment = models.CharField(max_length=500, default='')
     user_name = models.CharField(max_length=200, default='')
     user_email = models.CharField(max_length=200, default='')
     project_type = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
     verification = models.CharField(max_length=200, default='Unverified')
     
     def __str__(self):
          return self.user_name
     


class QuoteRequest(models.Model):
     project_type = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
     user_name = models.CharField(max_length=200, default='')
     user_email = models.CharField(max_length=200, default='')
     project_desc = models.CharField(max_length=2000, default='')
     budget = models.DecimalField(max_digits=6, decimal_places=2)
     final_price = models.DecimalField(max_digits=6, decimal_places=2)
     status = models.CharField(max_length=200, default='Requested')

     def __str__(self):
          return self.user_name