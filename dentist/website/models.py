from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

#class Customer(models.Model):
#    fname = models.CharField(max_length=200)

class Nurse(models.Model):
    fname = models.CharField('Nurse First Name', max_length=200)
    lname = models.CharField('Nurse Last Name', max_length=200)
    phone = models.CharField('Nurse Phone', max_length=25)
    email = models.EmailField('Nurse Email', max_length=25)

    def __str__(self):
        return self.fname + ' ' + self.lname


class Dentist(models.Model):
    DEGREES = (
        ('BA', 'Bachelors'),
        ('MA', 'Masters'),
        ('DR', 'PhD'),
    )
    COLLEGES = (
        ('CUN', 'CUNY'),
        ('NYU', 'NYU'),
        ('MIT', 'MIT'),
    )
    fname = models.CharField('Doctor First Name', max_length=200, null=True)
    lname = models.CharField('Doctor Last Name', max_length=200, null=True)
    qualification = models.CharField('Doctor Degree',max_length=2, choices=DEGREES, null=True)
    college = models.CharField('Doctor College', max_length=3, choices=COLLEGES, null=True)
    experience_yrs = models.IntegerField('Doctor Experience yrs', null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname 


class Venue(models.Model):
    vname = models.CharField('Venue Name', max_length=200)
    address = models.CharField('Venue Physical Address', max_length=300)
    zip_code = models.CharField('Venue Zip Code', max_length=15)
    phone = models.CharField('Venue Phone', max_length=25)
    web = models.URLField('Venue Website Address')
    email_address = models.EmailField('Venue Email Address')
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    owner = models.IntegerField('Venue Owner', blank=False, default=1)
    venue_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.vname 

class Upcomming_apt(models.Model):
    doc = models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    fname = models.CharField('Customer First Name', max_length=200)
    lname = models.CharField('Customer Last Name', max_length=200)
    phone_number = models.CharField('Customer Phone Number', max_length=25)
    email_address = models.EmailField('Customer Email', max_length=25)
    apt_time = models.DateTimeField('Appointment Time')
    nurses = models.ManyToManyField(Nurse, blank=True)
    is_done = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    #assistance_tracker = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL )
    approved = models.BooleanField("Approved",default=False)

    def __str__(self):
        return self.fname 
    
    @property
    def Days_till(self):
        today = date.today()
        days_till = self.apt_time.date()-today
        days_till = str(days_till).split(",",1)[0]
        return days_till

    @property 
    def Is_past(self):
        today = date.today()
        if self.apt_time.date() < today:
            res = "past due"
        else:
            res = "future"
        return res

class Finished_apt(models.Model):
    doc = models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    fname = models.CharField('Customer First Name', max_length=200, blank=True, null=True)
    lname = models.CharField('Customer Last Name', max_length=200, blank=True, null=True)
    phone_number = models.CharField('Customer Phone Number', max_length=25, blank=True, null=True)
    email_address = models.EmailField('Customer Email', max_length=25, blank=True, null=True)
    apt_time = models.DateTimeField('Appointment Time', blank=True, null=True)
    nurses = models.ManyToManyField(Nurse , blank=True, null=True)
    is_done = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    #assistance_tracker = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL )

    def __str__(self):
        return self.fname 

class Htmldata(models.Model):
    data_link = models.CharField('Data Link', max_length=200)
    data_name = models.CharField('Data Name', max_length=200)

    def __str__(self):
        return self.data_link 

class Webdata(models.Model):
    firstname = models.CharField('First Name', max_length=200)
    lastname = models.CharField('Last Name', max_length=200)
    querytime = models.DateTimeField('Query Time', blank=True, null=True)
    querysite = models.URLField('Website to Query')

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Cppdata(models.Model):
    file_name = models.CharField('File Name', max_length=200)
    file_location = models.CharField('File Location', max_length=200)
    file_extension = models.CharField('File Extension', max_length=200)
    def __str__(self):
        return self.file_name + ' ' + self.file_location + '' + self.file_extension

class Jobdata(models.Model):
    DEGREES = (
        ('BA', 'Bachelors'),
        ('MA', 'Masters'),
        ('DR', 'PhD'),
    )
    POSITION = (
        ('RN', 'NURSE'),
        ('TEC', 'TECHNICIAN'),
        ('DEN', 'DENTIST'),
    )
    position= models.CharField('Position', max_length=20, choices=POSITION, null=False)
    fname = models.CharField('First Name', max_length=200)
    lname = models.CharField('Last Name', max_length=200)
    phone_number = models.CharField('Phone Number', max_length=25)
    email_address = models.EmailField('Email', max_length=25)
    education= models.CharField('Education', max_length=20, choices=DEGREES, null=False)
    age = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.fname + ' ' + self.lname
    

