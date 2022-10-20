from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from . models import Venue, Upcomming_apt, Dentist
from . import forms 

def events(request):
    event_list = Upcomming_apt.objects.all()
    dentist_list = Dentist.objects.all()
    venue_list = Venue.objects.all()
    missed_apt_list = Upcomming_apt.objects.filter(is_done=0)

    submitted_dentist = False
    submitted_venue = False
    #form = forms.DentistForm2
    #form2 = forms.VenueForm
    #dentistform = forms.DentistForm2(request.POST)
    #venueform=forms.VenueForm(request.POST)
    if request.method=='POST':
        #form = forms.DentistForm2(request.POST)
        dentistform = forms.DentistForm2(request.POST)
        venueform=forms.VenueForm(request.POST)
        if dentistform.is_valid():
            dentistform.save()
            return HttpResponseRedirect('/events.html?submitted_dentist=True')
        else:
            if venueform.is_valid():
                venueform.save()
                return HttpResponseRedirect('/events.html?submitted_venue=True')
    else:
        dentistform = forms.DentistForm2
        venueform = forms.VenueForm
        if 'submitted_dentis' in request.GET:
            submitted_dentist = True
        elif 'submitted_venue' in request.GET:
            submitted_venue = True
    
    return render(request, "events.html",{"event_list":event_list,"dentist_list":dentist_list,
    "venue_list":venue_list,
     "dentistform":dentistform,"venueform":venueform, "submitted_dentist":submitted_dentist,
     "submitted_venue":submitted_venue, "missed_apt_list":missed_apt_list})


def home(request):
    return render(request,"base.html")

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        '''
        #send an email
        send_mail(
            'message from' + message_name , # email subject
            message , # email body
            message_email , # from email
            ['tmuthoka@gmail.com','terrence.muthoka@citi.com'], # to emai;
        )
        '''
        return render(request,"contact.html",{'message_name':message_name})

    else:
        return render(request,"contact.html",{})


def about(request):
    return render(request,"about.html")

def blog_details(request):
    return render(request,"blog-details.html")

def blog(request):
    return render(request,"blog.html")

def pricing(request):
    return render(request,"pricing.html")

def service(request):
    return render(request,"service.html")


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']
        
        '''
        #send an email
        send_mail(
            'Hello ' + your_name , # email subject
            'your appointment is at ' + your_time , # email body
            'please confirm this message: '+ your_message , # from email
            ['tmuthoka@gmail.com','terrence.muthoka@citi.com'], # to emai;
        )
        '''

        text_file = open("address_test.txt", "w")
        n = text_file.write(your_address)
        text_file.close()

        

        return render(request,"appointment.html",{
            'your_name':your_name, 
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_time':your_time,
            'your_message':your_message
            })

    else:
        return render(request,"base.html",{})





