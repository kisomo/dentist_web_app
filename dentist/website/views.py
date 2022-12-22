from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, StreamingHttpResponse, FileResponse
from django.core.mail import send_mail
from . models import Venue, Upcomming_apt, Dentist, Webdata, Cppdata, Htmldata
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
    p = Paginator(Upcomming_apt.objects.all().order_by("-apt_time","lname"), 3)
    page_num = request.GET.get("page",1)
    event_list = p.get_page(page_num)
    #apt_nums = "a"*event_list.paginator.num_pages
    apt_nums = "a"*p.num_pages

    dentist_list = Dentist.objects.all().order_by("lname")
    venue_list = Venue.objects.all().order_by("vname")
    missed_apt_list = Upcomming_apt.objects.filter(is_done=0)

    submitted_dentist = False
    submitted_venue = False
    submitted_web = False
    submitted_cpp = False
    submitted_html = False
    
    if request.method=='POST':
        #form = forms.DentistForm2(request.POST)
        dentistform = forms.DentistForm2(request.POST)
        venueform=forms.VenueForm(request.POST)
        form_data = forms.WebdataForm(request.POST)
        cpp_data = forms.CppdataForm(request.POST)
        html_data = forms.HtmldataForm(request.POST)
        #if all([dentistform.is_valid(),venueform.is_valid()]):
        if dentistform.is_valid():
            dentistform.save()
            #venueform.save()
            return HttpResponseRedirect('/events.html?submitted_dentist=True')
            #return HttpResponseRedirect('/events.html?submitted_dentist=True?submitted_venue=True')
        elif venueform.is_valid():
            venueform.save()
            return HttpResponseRedirect('/events.html?submitted_venue=True')
        elif html_data.is_valid():
            html_data.save()
            return HttpResponseRedirect('/events.html?submitted_html=True')
        #elif 'py2' in request.POST:
        elif form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect('/events.html?submitted_web=True')
        elif cpp_data.is_valid():
            cpp_data.save()
            return HttpResponseRedirect('/events.html?submitted_cpp=True')
        else:
            #return render(request, "events.html",{})
            return HttpResponseRedirect('/events.html')
    else:
        dentistform = forms.DentistForm2
        venueform = forms.VenueForm
        form_data = forms.WebdataForm()
        cpp_data = forms.CppdataForm()
        html_data = forms.HtmldataForm()
        if 'submitted_dentist' in request.GET:
            submitted_dentist = True
        elif 'submitted_venue' in request.GET:
            submitted_venue = True
        elif 'submitted_web' in request.GET:
            submitted_web = True
        elif 'submitted_cpp' in request.GET:
            submitted_cpp = True
        elif 'submitted_html' in request.GET:
            submitted_html = True
    
    return render(request, "events.html",{"event_list":event_list,"dentist_list":dentist_list,
    "venue_list":venue_list,
     "dentistform":dentistform,"venueform":venueform, "submitted_dentist":submitted_dentist,
     "submitted_venue":submitted_venue,"submitted_web":submitted_web, "submitted_cpp":submitted_cpp,
     "submitted_html":submitted_html,
     "missed_apt_list":missed_apt_list, "apt_nums":apt_nums, "form_data":form_data, "cpp_data":cpp_data,
     "html_data":html_data})


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
    #ata1 = requests.get("https://kitui.go.ke/countygovt/opportunities/tenders/")
    data1 = requests.get("https://www.google.com/")
    if data1:
        web_data = data1.text
        #web_data = data1.json()
        #web_data = data1.headers['content-type']
        return render(request, "events.html", {"web_data":web_data})
    return render(request, "events.html", {})

import sys, os, subprocess, calendar, datetime
from calendar import HTMLCalendar
from subprocess import run, PIPE
def external_py(request):
    if 'py' in request.POST:
        inp = request.POST.get('py')
        out = run([sys.executable, '/home/terrence/MODELS/dentist/dentist/website/tests.py',inp], 
        shell=False, stdout=PIPE)
        #print(out)
        return render(request, 'events.html',{"web_data2":out.stdout})
    return render(request, 'events.html')

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
    if 'cpp' in request.POST:
        inp = request.POST.get('cpp')
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
    return render(request, 'events.html')


def getWebdata(request):
    form_data = forms.WebdataForm()
    #   if form_data.is_valid():
    #        form_data.save()
    #        return HttpResponseRedirect('events.html')
    return render(request, "events.html",{"form_data":form_data})
    #return render(request, "events.html",{})

def search_venues(request):
    if request.method=='POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(zip_code=searched)
        return render(request, "search_venues.html",{"searched":searched,
        "venues":venues})
    else:
        return render(request, "search_venues.html",{})

def update_appt(request, upcomming_apt_id):
    appt = Upcomming_apt.objects.get(pk=upcomming_apt_id)
    form = forms.Upcoming_aptForm(request.POST or None, instance=appt)
    if form.is_valid():
        form.save()
        return redirect('events')
    return render(request, "update_appt.html",{"appt":appt,"form":form})



