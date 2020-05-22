from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Job, Vistor, Services, ServicePoints, Testimonial, QuoteRequest
import requests
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    jobs = Job.objects
    last_visitor = Vistor.objects.all().last()
    location_now = last_visitor.location
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"#convert location to weather
    querystring = { "q":location_now,
                    "appid":"f2c22ffb64b399b3a2aecccfe3fd34f4"
                    }
    weather_response = requests.request("GET", weather_url, params=querystring)
    weather = weather_response.json()
    return render(request, 'jobs/home.html', 
                    {'jobs':jobs,
                    'location':location_now,
                    'pressure':weather["main"]["pressure"],
                    'humidity':weather["main"]["humidity"],
                    'temp_min':round(weather["main"]["temp_min"] - 273.15,2),
                    'temp_max':round(weather["main"]["temp_max"] - 273.15,2),
                    'icon':weather["weather"][0]["icon"]
                    })


def visitor_count(request):
    print('____________________')
    if request.method == 'GET':
        print(request.POST['ip_address'])
        visitor = Vistor()
        userip = request.GET['ip_address']
        visitor.userip = userip[2:]
        visitor.location = location_now
        visitor.visit_date = timezone.datetime.now()
        visitor.save()
        print('added')
    print('not added')
    return HttpResponse('Success')


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us \n testing the newline \n testing again'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['me@aneeshbharath.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('Success')


def services(request):
    services = Services.objects
    servicespoints = ServicePoints.objects
    Testimonials = Testimonial.objects.filter(verification='verified')
    return render(request, 'jobs/services.html', {  'services':services, 
                                                    'servicespoints':servicespoints,
                                                    'Testimonials':Testimonials})

def addTestimonials(request):
    if request.method == 'POST':
        testimonial = Testimonial()
        testimonial.image = request.FILES['userimage']
        testimonial.comment = request.POST['comment']
        testimonial.user_name = request.POST['username']
        testimonial.user_email = request.POST['useremail']
        testimonial.save()
        subject = 'New Testimonial Added to WebPortfolio!'
        message = 'A New testimonial was added to the Webportfolio application. \n Name: {}. \n Email: {}. \n Message: {}'.format( request.POST['username'], request.POST['useremail'], request.POST['comment'])
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['me@aneeshbharath.com',]
        send_mail( subject, message, email_from, recipient_list )
        messages.info(request, 'Thankyou for your feedback, your Testimonial will be displayed soon!')
    return HttpResponseRedirect('/services')


def addQuoteRequest(request):
    if request.method == 'POST':
        quotes = QuoteRequest()
        service_id = request.POST['proj_type']
        service_name = Services.objects.get(id = request.POST['proj_type'])
        quotes.project_type = Services.objects.get(id = request.POST['proj_type'])
        quotes.user_name = request.POST['username']
        quotes.user_email = request.POST['useremail']
        quotes.project_desc = request.POST['description']
        quotes.budget = request.POST['proj_budget']
        quotes.final_price = 00
        quotes.save()
        subject = 'New Quote Request has been recieved!'
        message = 'A New Quote Request has been recieved for {}. \n Name: {}. \n Email: {}. \n Message: {}'.format( service_name.service_title, request.POST['username'], request.POST['useremail'], request.POST['description'])
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['me@aneeshbharath.com',]
        send_mail( subject, message, email_from, recipient_list )
        messages.info(request, 'Your Quote has been submitted, We will contact you soon!')
    return HttpResponseRedirect('/services')




    
'''
        ip_toLocation = "https://ip-geo-location.p.rapidapi.com/ip/" + ip_address[2][3:]
        querystring_ip = {"format":"json"}
        headers_ip = {
            'x-rapidapi-host': "ip-geo-location.p.rapidapi.com",
            'x-rapidapi-key': "567ab5fe7bmsh396072837da1a2cp161316jsnb5774dba1784"
            }
        response_ip = requests.request("GET", ip_toLocation, headers=headers_ip, params=querystring_ip)
        response_ip = response_ip.json()
        location_now = response_ip['area']['name']
'''