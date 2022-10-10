from django.db import models

# Create your models here.

class Customer(models.Model):
    fname = models.CharField(max_length=200)

class Dentist(models.Model):
    fname = models.CharField(max_length=200)

class Venue(models.Model):
    vname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    web = models.URLField()
    email_address = models.EmailField()


class Upcomming_apt(models.Model):
    doc = models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    apt_time = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.fname 

class Finished_apt(models.Model):
    fname = models.CharField(max_length=200)



