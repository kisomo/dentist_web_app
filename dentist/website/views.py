from django.shortcuts import render
from django.core.mail import send_mail
from . models import Venue

def events(request):
    event_list = Venue.objects.all()
    return render(request, "events.html",{"event_list":event_list})

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





