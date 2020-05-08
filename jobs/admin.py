from django.contrib import admin

# Register your models here.

from .models import Job
from .models import Vistor

admin.site.register(Job)
admin.site.register(Vistor)