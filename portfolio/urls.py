
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('jobsapi/', include('jobs.urls'), name='home'),
    path('services/', jobs.views.services, name='services'),
    path('jobs/addTestimonials', jobs.views.addTestimonials, name='addTestimonials'),
    path('jobs/addQuoteRequest', jobs.views.addQuoteRequest, name='addQuoteRequest'),
    path('jobs/visitor_count', jobs.views.visitor_count, name='visitor_count'),
    path('jobs/email', jobs.views.email, name='send_mail'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('blog/', include('blog.urls'), name='blog'),
    path('contact/', include('contact.urls'), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
