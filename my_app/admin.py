from django.contrib import admin
from .models import Contact  # Import the Contact model

# Register your models here.
admin.site.register(Contact)
admin.site.site_header = "My Personal Portfolio Website| Admin Panel"
admin.site.site_title = "Admin Panel"