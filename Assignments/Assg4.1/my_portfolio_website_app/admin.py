#<--- My Portfolio Website - Imported Packages List ----

#------Django Internal Packages-----
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
#/------Django Internal Packages-----

#------Django Importing Models-----
from my_portfolio_website_app.models import ContactForm,CustomUser
#/------Django Importing Models-----


#</--- My Portfolio Website - Imported Packages List ----


#Register your models here.


#-----Django Admin View for ----

#Django Admin View for Contact Form Model
class ContactFormkAdmin(ImportExportModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "contact_number",
        "message",
    ]
    list_editable = ["full_name"]


#Register ContactForm in Admin view 
admin.site.register(ContactForm,ContactFormkAdmin)
#Register CustomUser in Admin view 
admin.site.register(CustomUser)