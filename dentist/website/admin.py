from django.contrib import admin
from django.contrib.auth.models import Group

from . models import Venue, Upcomming_apt, Finished_apt, Dentist, Nurse, Webdata,Cppdata, Htmldata, Jobdata
from .models import Interview

admin.site.register(Finished_apt)
#admin.site.unregister(Group)


#admin.site.register(Venue)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("vname","address","zip_code", "phone","web")
    ordering = ("vname",)
    search_fields = ("vname","address")

#admin.site.register(Nurse)
@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","phone","email")
    ordering = ("fname",)
    search_fields = ("fname","phone")


#@admin.register(Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","qualification","college", "experience_yrs")
    ordering = ("fname",)
    search_fields = ("fname","experience_yrs")
admin.site.register(Dentist, DentistAdmin)

class upcoming_apt_Admin(admin.ModelAdmin):
    fields = (("venue","fname","lname","doc"),"phone_number","email_address","apt_time",
    "nurses","is_done","description","approved") #,"assistance_track")
    list_display = ("venue","fname","lname","doc","phone_number","email_address",
    "apt_time","approved")
    list_filter = ("apt_time","venue")
    ordering = ("fname",)
admin.site.register(Upcomming_apt, upcoming_apt_Admin)

admin.site.register(Webdata)

admin.site.register(Cppdata)

admin.site.register(Htmldata)

admin.site.register(Jobdata)

admin.site.register(Interview)

