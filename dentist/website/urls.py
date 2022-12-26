
#from django.contrib import admin
from django.urls import path
from . import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base.html', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('blog-details.html', views.blog_details, name='blog_details'),
    path('blog.html', views.blog, name='blog'),
    path('pricing.html', views.pricing, name='pricing'),
    path('service.html', views.service, name='service'),
    path('appointment.html', views.appointment, name='appointment'),
    path('events.html', views.events, name='events'),
    path(r'web_output', views.web_output, name='web_script'),
    path(r'external_py/', views.external_py, name='external_py'),
    path(r'external_cpp/', views.external_cpp, name='external_cpp'),
    path(r'getWebdata/', views.getWebdata, name='getWebdata'),
    path('search_venues', views.search_venues, name='search-venues'),
    path('update_appt/<upcomming_apt_id>', views.update_appt, name='update-appt'),
    path('delete_appt/<appointment_id>', views.delete_appt, name='delete-appt'),
    path('appointment_txt', views.appointment_txt, name='appointment-txt'),
    path('appointment_csv', views.appointment_csv, name='appointment-csv'),
    path('appointment_pdf', views.appointment_pdf, name='appointment-pdf'),
    path('my_appts', views.my_appts, name='my-appts'),
    path('admin_approval', views.admin_approval, name='admin-approval'),
    path('venue_appts/<venue_id>', views.venue_appts, name='venue-appts'),
    path('appt_details/<appt_id>', views.appt_details, name='appt-details'),
    path('apply_job>', views.apply_job, name='apply-job'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





