from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    last_blog = Blog.objects.all().last()
    return render(request, 'blog/allblogs.html',{'blogs':blogs, 'last_blog':last_blog})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : detailblog})
