from django.contrib import admin

# Register your models here.
from .models import Blog
from .models import Subject

admin.site.register(Blog)
admin.site.register(Subject)