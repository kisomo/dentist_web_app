from django.db import models

# Create your models here.

#class Customer(models.Model):
#    fname = models.CharField(max_length=200)

class Nurse(models.Model):
    fname = models.CharField('Nurse First Name', max_length=200)
    lname = models.CharField('Nurse Last Name', max_length=200)
    phone = models.CharField('Nurse Phone', max_length=25)
    emial = models.EmailField('Nurse Email', max_length=25)

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

    def __str__(self):
        return self.vname 

class Upcomming_apt(models.Model):
    doc = models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    fname = models.CharField('Customer First Name', max_length=200)
    lname = models.CharField('Customer Last Name', max_length=200)
    phone_number = models.CharField('Customer Phone Number', max_length=25)
    email_address = models.EmailField('Customer Email', max_length=25)
    apt_time = models.DateTimeField('Appointment Time')
    nurses = models.ManyToManyField(Nurse, blank=True)
    is_done = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.fname 

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

    def __str__(self):
        return self.fname 



