from django.contrib import admin

# Register your models here.

from .models import Job, Vistor, JobImage, Services, ServicePoints, Testimonial

admin.site.register(Job)
admin.site.register(Vistor)
admin.site.register(JobImage)
admin.site.register(Services)
admin.site.register(ServicePoints)
admin.site.register(Testimonial)
