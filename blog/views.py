from django.shortcuts import render, get_object_or_404
import requests
from .models import Blog
from .models import testTable


def allblogs(request):
    blogs = Blog.objects
    items = testTable.objects
    last_blog = Blog.objects.all().last()
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = { "id":"2172797",
                    "units":"metric",
                    "q":"London,uk"
                    }
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "1fe53a3500msh648ee33bcb45224p1791e1jsne51a930b6e9e"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
    weather = response.json()
    return render(request, 'blog/allblogs.html',{'blogs':blogs, 'last_blog':last_blog, 'items':items, 'weather':weather})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : detailblog})



