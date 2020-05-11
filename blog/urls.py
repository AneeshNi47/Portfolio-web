from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.allblogs, name='allblogs'),
    path('<str:blog_title>/', views.detail, name='detail')
] 