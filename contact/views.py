from django.shortcuts import render, redirect
from .models import Contact
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import jobs.views

# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.subject = request.POST['subject']
        contact.message = request.POST['message']
        contact.status = "Open"
        contact.contact_date = timezone.datetime.now()
        contact.save()
        messages.info(request, 'Your Message has been sent, We will contact you soon!')
        return HttpResponseRedirect('/contact')
    else:
        return render(request, 'contact.html')

def success(request):
    return render(request, 'success.html')