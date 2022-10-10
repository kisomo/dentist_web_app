from django.contrib import admin
from . models import Venue, Customer, Upcomming_apt, Finished_apt, Dentist

admin.site.register(Venue)
admin.site.register(Customer)
admin.site.register(Upcomming_apt)
admin.site.register(Finished_apt)
admin.site.register(Dentist)


