from django.shortcuts import render, get_object_or_404
import requests
from .models import Blog

def allblogs(request):
    x_forwarded_for = request.META.get('REMOTE_HOST')
    keys = request.META.values()
    print(keys)
    print(x_forwarded_for)
    blogs = Blog.objects
    last_blog = Blog.objects.all().last()
    url_ip = "https://ip-geo-location.p.rapidapi.com/ip/" + str(x_forwarded_for)
    url_new = "https://ip-geo-location.p.rapidapi.com/ip/202.83.42.255"
    print(url_ip)
    print(url_new)
    querystring_ip = {"format":"json"}
    headers_ip = {
        'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
        'x-rapidapi-key': "567ab5fe7bmsh396072837da1a2cp161316jsnb5774dba1784"
        }
    response_ip = requests.request("GET", url_ip, headers=headers_ip, params=querystring_ip)
    response_ip = response_ip.json()
    url = "https://api.openweathermap.org/data/2.5/weather?"
    querystring = { "q":"Kerala",
                    "appid":"f2c22ffb64b399b3a2aecccfe3fd34f4"
                    }
    response = requests.request("GET", url, params=querystring)
    weather = response.json()
    return render(request, 'blog/allblogs.html',
                    {
                        'blogs':blogs, 
                        'last_blog':last_blog, 
                        'weather':weather,
                        'weather_desc':weather["weather"][0]["description"], 
                        'addres':response_ip, 
                        'ip_addres':x_forwarded_for
                        }
                    )

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : detailblog})