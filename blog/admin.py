from django.contrib import admin

# Register your models here.
from .models import Blog
from .models import testTable

admin.site.register(Blog)
admin.site.register(testTable)