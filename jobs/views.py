from django.shortcuts import render
from .models import Job
from .models import Vistor
import requests
from django.utils import timezone
# Create your views here.

def home(request):
    jobs = Job.objects
    last_visitor = Vistor.objects.all().last()
    # get user ip address
    url_ip = "https://www.cloudflare.com/cdn-cgi/trace"
    response_ip = requests.request("GET", url_ip)
    ip_address = response_ip.text.split()
    if last_visitor:
        #convert IP to location
        ip_toLocation = "https://ip-geo-location.p.rapidapi.com/ip/" + ip_address[2][3:]
        querystring_ip = {"format":"json"}
        headers_ip = {
            'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
            'x-rapidapi-key': "567ab5fe7bmsh396072837da1a2cp161316jsnb5774dba1784"
            }
        if last_visitor.userip != ip_address[2][3:]:
            response_ip = requests.request("GET", ip_toLocation, headers=headers_ip, params=querystring_ip)
            response_ip = response_ip.json()
            print(response_ip['area']['name'])
            #convert location to weather
            weather_url = "https://api.openweathermap.org/data/2.5/weather?"
            querystring = { "q":response_ip['area']['name'],
                            "appid":"f2c22ffb64b399b3a2aecccfe3fd34f4"
                            }
            weather_response = requests.request("GET", weather_url, params=querystring)
            weather = weather_response.json()
            print(weather["weather"][0])
            print(weather["main"]["temp"])
            print(weather["main"]["pressure"])
            print(weather["main"]["humidity"])
            visitor = Vistor()
            visitor.userip = ip_address[2][3:]
            visitor.location = response_ip['area']['name']
            visitor.visit_date = timezone.datetime.now()
            visitor.save()
            print(ip_address[2][3:])
        else:
            print("User already present")
    else:
        visitor = Vistor()
        visitor.userip = ip_address[2][3:]
        visitor.save()

    return render(request, 'jobs/home.html', {'jobs':jobs})


#'weather_desc':
def visitor_count(request):
    print('not added')
    if request.method == 'POST':
        visitor = Vistor()
        userip = request.POST['ip_address']
        visitor.userip = userip[2:]
        visitor.visit_date = timezone.datetime.now()
        visitor.save()
        print('added')
    print('not added')
    return HttpResponse('')
    