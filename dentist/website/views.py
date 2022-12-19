from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, StreamingHttpResponse, FileResponse
from django.core.mail import send_mail
from . models import Venue, Upcomming_apt, Dentist
from . import forms 
import csv 
import io 
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator

def events(request):
    #event_list = Upcomming_apt.objects.all().order_by("-apt_time","lname")
    # set up pagination
    p = Paginator(Upcomming_apt.objects.all().order_by("-apt_time","lname"), 2)
    page = request.GET.get("page")
    event_list = p.get_page(page)
    apt_nums = "a"*event_list.paginator.num_pages

    dentist_list = Dentist.objects.all().order_by("lname")
    venue_list = Venue.objects.all().order_by("vname")
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
     "submitted_venue":submitted_venue, "missed_apt_list":missed_apt_list,
     "apt_nums":apt_nums})


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


def delete_appointment(request, appointment_id):
    appointment = Upcomming_apt.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect("events.html")

def appointment_txt_file(request, submitted_id):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=appointments.txt'
    lines = [] #['This is line 1\n','This is line 2\n']
    appointments = Upcomming_apt.objects.all()
    for appointment in appointments:
        lines.append(f'{appointment.doc}\n{appointment.venue}\n{appointment.fname}\n\n')
    response.writelines(lines)
    return response

def appointment_csv_file(reuqest, submitted_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=appointments.csv'
    writer = csv.writer(response)

    #lines = [] #['This is line 1\n','This is line 2\n']
    appointments = Upcomming_apt.objects.all()
    # add column headings 
    writer.writerow(['Doctor', 'Venue', 'First Name'])
    for appointment in appointments:
        writer.writerow([appointment.doc, appointment.venue, appointment.fname])
    return response

def appointment_pdf_file(request, submitted_id):
    #create bytestream buffer
    buf = io.BytesIO()
    # create canvas
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    #create the text object
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFront("Helvetica", 14)

    lines = [] #['This is line 1\n','This is line 2\n']
    appointments = Upcomming_apt.objects.all()
    for appointment in appointments:
        lines.append(appointment.doc)
        lines.append(appointment.venue)
        lines.append(appointment.fname)
        lines.append("=====================================================")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='appointments.pdf')


def web_output(request):
    import requests
    data1 = requests.get("https://kitui.go.ke/countygovt/opportunities/tenders/")
    #data1 = requests.get("https://www.google.com/")
    web_data = data1.text
    #web_data = data1.json()
    #web_data = data1.headers['content-type']
    return render(request, "events.html", {"web_data":web_data})

import sys, os, subprocess
from subprocess import run, PIPE
def external_py(request):
    inp = request.POST.get('param')
    out = run([sys.executable, '/home/terrence/MODELS/dentist/dentist/website/tests.py',inp], 
    shell=False, stdout=PIPE)
    print(out)
    return render(request, 'events.html',{"web_data2":out.stdout})

def external_cpp(request):
    '''
    inp = request.POST.get('param')
    out = run([sys.executable, '/home/terrence/MODELS/dentist/dentist/website/tests.py',inp], 
    shell=False, stdout=PIPE)
    print(out)
    return render(request, 'events.html',{"web_data2":out.stdout})
    '''
    # create a pipe to a child process
    data, temp = os.pipe()
    
    inp = request.POST.get('param')
    # write to STDIN as a byte object(convert string
    # to bytes with encoding utf8)
    os.write(temp, bytes("5 10\n", "utf-8"));
    os.close(temp)
    # store output of the program as a byte string in s
    out = subprocess.check_output("g++ /home/terrence/MODELS/dentist/dentist/website/split_string.cpp -o out2;./out2", 
    stdin = data, shell = True)
    # decode s to a normal string
    print(out.decode("utf-8"))
    return render(request, 'events.html',{"web_data3":out})



