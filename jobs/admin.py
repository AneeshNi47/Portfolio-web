from django.contrib import admin

# Register your models here.

from .models import Job
from .models import Vistor
from .models import JobImage

admin.site.register(Job)
admin.site.register(Vistor)
admin.site.register(JobImage)