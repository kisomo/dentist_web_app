
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

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

