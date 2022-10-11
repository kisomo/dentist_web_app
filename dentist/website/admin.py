from django.contrib import admin
from . models import Venue, Upcomming_apt, Finished_apt, Dentist, Nurse #, Customer

admin.site.register(Venue)
#admin.site.register(Customer)
admin.site.register(Nurse)
admin.site.register(Upcomming_apt)
admin.site.register(Finished_apt)
admin.site.register(Dentist)


