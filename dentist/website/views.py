from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, StreamingHttpResponse, FileResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from . models import Venue, Upcomming_apt, Dentist, Webdata, Cppdata, Htmldata, Interview
from . import forms 
import csv 
import io 
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.contrib.auth.models import User

from django.core.paginator import Paginator
from django.contrib import messages

def events(request):
    #event_list = Upcomming_apt.objects.all().order_by("-apt_time","lname")
    # set up pagination
    p = Paginator(Upcomming_apt.objects.all().order_by("-apt_time","lname"), 3)
    page_num = request.GET.get("page")
    event_list = p.get_page(page_num)
    #apt_nums = "a"*event_list.paginator.num_pages
    apt_nums = "a"*p.num_pages

    dentist_list = Dentist.objects.all().order_by("lname")
    venue_list = Venue.objects.all().order_by("vname")
    interview_list = Interview.objects.all()
    
    missed_apt_list = Upcomming_apt.objects.filter(is_done=0)

    submitted_dentist = False
    submitted_venue = False
    submitted_web = False
    submitted_cpp = False
    submitted_html = False
    
    if request.method=='POST':
        #form = forms.DentistForm2(request.POST)
        dentistform = forms.DentistForm2(request.POST)
        venueform=forms.VenueForm(request.POST, request.FILES)
        venueform.owner = request.user.id

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
        dentistform = forms.DentistForm2()
        venueform = forms.VenueForm()
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
    
    return render(request, "events.html",{"event_list":event_list,
    "dentist_list":dentist_list,
    "venue_list":venue_list,"interview_list":interview_list,
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


def delete_appt(request, appointment_id):
    appointment = Upcomming_apt.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect("events")

def appointment_txt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=appointments.txt'
    lines = [] #['This is line 1\n','This is line 2\n']
    appointments = Upcomming_apt.objects.all()
    for appointment in appointments:
        lines.append(f'{appointment.doc}\n{appointment.venue}\n{appointment.fname}\n\n')
    response.writelines(lines)
    return response

def appointment_csv(reuqest):
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

def appointment_pdf(request):
    #create bytestream buffer
    buf = io.BytesIO()
    # create canvas
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    #create the text object
    textob= c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

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
        owners =[]
        for venue in venues:
            owners.append(User.objects.get(pk=venue.owner))
        return render(request, "search_venues.html",{"searched":searched,
        "venues":venues, "owners":owners})
    else:
        return render(request, "search_venues.html",{})

def update_appt(request, upcomming_apt_id):
    appt = Upcomming_apt.objects.get(pk=upcomming_apt_id)
    #appt.manager = request.user.id
    form = forms.Upcoming_aptForm(request.POST or None, request.FILES or None, instance=appt)
    if form.is_valid():
        form.save()
        return redirect('events')
    return render(request, "update_appt.html",{"appt":appt,"form":form})


def my_appts(request):
    event = Upcomming_apt.objects.get(doc=request.user.id)
    return render(request,"my_appts.html",{"event":event})

def admin_approval(request):
    #get venues
    venues = Venue.objects.all()
    

    appts_count = Upcomming_apt.objects.all().count()
    venue_count = Venue.objects.all().count()
    dentist_count = Dentist.objects.all().count()

    appts = Upcomming_apt.objects.all().order_by('-apt_time')

    if request.user.is_superuser:
        if request.method=="POST":
            id_list = request.POST.getlist('boxes')
            #uncheck all appointments
            appts.update(approved=False)
            #update the database
            for x in id_list:
                Upcomming_apt.objects.filter(pk=int(x)).update(approved=True)
            messages.success(request,"Appt list approval submitted")
            return redirect('events')
        else:
            return render(request,"admin_approval.html",{"appts":appts,
            "appts_count":appts_count,"venue_count":venue_count,"dentist_count":dentist_count,
            "venues":venues})
    else:
        messages.success(request,"Access Denied")
        return redirect('events')

def venue_appts(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    appts = venue.upcomming_apt_set.all()
    if appts:
        return render(request,"venue_appts.html",{"appts":appts})
    else:
        messages.success(request,"No Appointments for this venue")
        return redirect('admin-approval')
    
def appt_details(request, appt_id):
    appts = Upcomming_apt.objects.get(id=appt_id)
    return render(request,"appt_details.html",{"appts":appts})

def apply_job(request):
    if request.method=="POST":
        form = forms.JobdataForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            position = request.POST['position']
            fname = request.POST['fname']
            lname = request.POST['lname']
            phone_number = request.POST['phone_number']
            email_address = request.POST['email_address']
            education= request.POST['education']
            age = request.POST['age']
            description = request.POST['description']

            messages.success(request,("There was an error please try again"))
            #return redirect("events")
            return render(request, "events.html",{"position":position,"fname":fname,
            "lname":lname,"phone_number":phone_number,"email_address":email_address,
            "education":education,"age":age,"description":description})
        messages.success(request,("application submitted"))
        return redirect("events")
    else:
        return render(request,"events.html",{})


def interview_add(request):
    interviews = Interview.objects.all()
    if request.method=="POST":
        inter_form = forms.InterviewForm(request.POST)
        if inter_form.is_valid():
            inter_form.save()
            return redirect('events')
    else:
        inter_form = forms.InterviewForm()
    return render(request, "events.html",{"inter_form":inter_form,
    "interviews":interviews})

#def interviews_all(request):
#    interviews = Interview.objects.all()
#    return render(request, "events.html",{"interviews":interviews})

def interview_edit(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    if request.method=="POST":
        form = forms.InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            #return redirect('events')
            return HttpResponse(form.as_p())
    else:
        form = forms.InterviewForm(instance=interview)
    return render(request, "events.html",{"InterviewForm":form,"interview":interview})

#def interview_list(request):
#    return render(request, "interview_list.html",{
#        "interviews_list":Interview.objects.all()})




















