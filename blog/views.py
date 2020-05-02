from django.shortcuts import render, get_object_or_404
import requests
from .models import Blog
from .models import testTable

def allblogs(request):
    x_forwarded_for = request.META.get('REMOTE_ADDR')
    print(x_forwarded_for)
    blogs = Blog.objects
    items = testTable.objects
    last_blog = Blog.objects.all().last()
    url_ip = "https://ip-geo-location.p.rapidapi.com/ip/{}".format(x_forwarded_for)
    print(url_ip)
    querystring_ip = {"format":"json"}
    headers_ip = {
        'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
        'x-rapidapi-key': "567ab5fe7bmsh396072837da1a2cp161316jsnb5774dba1784"
        }
    response_ip = requests.request("GET", url_ip, headers=headers_ip, params=querystring_ip)
    response_ip = response_ip.json()
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
    weather = response.json()
    return render(request, 'blog/allblogs.html',{'blogs':blogs, 'last_blog':last_blog, 'items':items, 
                    'weather':weather,'weather_desc':weather["weather"][0]["description"], 'addres':response_ip, 'ip_addres':x_forwarded_for})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : detailblog})