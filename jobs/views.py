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
        if last_visitor.userip != ip_address[2][3:]:
            check_now = True
        else:
            check_now = False
    else:
        check_now = True
    
    if check_now:
        #convert IP to location
        ip_toLocation = "https://ip-geo-location.p.rapidapi.com/ip/" + ip_address[2][3:]
        querystring_ip = {"format":"json"}
        headers_ip = {
            'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
            'x-rapidapi-key': "567ab5fe7bmsh396072837da1a2cp161316jsnb5774dba1784"
            }
        response_ip = requests.request("GET", ip_toLocation, headers=headers_ip, params=querystring_ip)
        response_ip = response_ip.json()
        location_now = response_ip['area']['name']
        print(response_ip['area']['name'])
        visitor = Vistor()
        visitor.userip = ip_address[2][3:]
        visitor.location = response_ip['area']['name']
        visitor.visit_date = timezone.datetime.now()
        visitor.save()
        print(ip_address[2][3:])
    else:
        print("User already present")
        location_now = last_visitor.location
    
    #convert location to weather
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"
    querystring = { "q":location_now,
                    "appid":"f2c22ffb64b399b3a2aecccfe3fd34f4"
                    }
    weather_response = requests.request("GET", weather_url, params=querystring)
    weather = weather_response.json()
    #print(location_now)
    #print(weather)
    #print(weather["weather"][0])
    #print(weather["main"]["temp"])
    #print(type(weather["main"]["temp_min"]))
    #print(weather["main"]["temp_max"])
    #print(weather["main"]["pressure"])
    #print(weather["main"]["humidity"])

    return render(request, 'jobs/home.html', 
                    {'jobs':jobs,
                    'location':location_now,
                    'pressure':weather["main"]["pressure"],
                    'humidity':weather["main"]["humidity"],
                    'temp_min':round(weather["main"]["temp_min"] - 273.15,2),
                    'temp_max':round(weather["main"]["temp_max"] - 273.15,2),
                    'icon':weather["weather"][0]["icon"]
                    })


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
    