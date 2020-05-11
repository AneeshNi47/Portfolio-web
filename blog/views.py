from django.shortcuts import render, get_object_or_404
import requests
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    last_blog = Blog.objects.all().last()
    return render(request, 'blog/allblogs.html',{'blogs':blogs,'last_blog':last_blog})


def detail(request, blog_title): 
    title_url = blog_title.replace("_", " ")
    detailblog = get_object_or_404(Blog, title=title_url)
    return render(request, 'blog/detail.html', {'blog' : detailblog})


    #url_ip = "https://ip-geo-location.p.rapidapi.com/ip/" + str(x_forwarded_for)
    #print(url_ip)
    #querystring_ip = {"format":"json"}
    #headers_ip = {
        #'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
        #'x-rapidapi-key': "567ab5fe7bmsh396072837da1a2cp161316jsnb5774dba1784"
        #}
    #response_ip = requests.request("GET", url_ip, headers=headers_ip, params=querystring_ip)
    #response_ip = response_ip.json()