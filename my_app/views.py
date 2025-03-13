from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import FileResponse
from django.conf import settings
import os
#Create your views here.
def Index(request):
    return render(request,"home.html")
def about_us(request):
    return render(request,"about.html")
def projects(request):
    return render(request,"project.html")
def experience(request):
    return render(request,"Experience.html")
def education(request):
    return render(request,"Education.html")
def certifications(request):
    return render(request,"certification.html")
#########################################################################
def contact(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Save data to the database
        contact_record = Contact(
            name=name,
            email=email,
            Phone_number=phone,
            message=message
        )
        contact_record.save()
        # Add a success message
        messages.success(request, "Your message has been submitted successfully!")
        return redirect('contact')  # Redirect to the contact page
    return render(request, "contact.html")
########################################################
def resume(request):
    resume_path = "myapp/resume1.pdf"
    
    # Get the absolute path of the file in the static folder
    full_path = staticfiles_storage.path(resume_path)
    
    # Check if the file exists at the path
    if staticfiles_storage.exists(resume_path):
        with open(full_path, "rb") as resume_file:
            # Create HTTP response with file content and set proper content type
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume1.pdf"'
            return response
    else:
        # Return a 404 response if file is not found
        return HttpResponse("Resume not found", status=404)
