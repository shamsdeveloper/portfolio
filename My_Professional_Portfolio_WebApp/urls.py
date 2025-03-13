from django.contrib import admin
from django.urls import path
from my_app import views as my_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',my_views.Index,name='Index'),
    path('my_about_us/',my_views.about_us,name='about_us'),
    path('my_projects/',my_views.projects,name='projects'),
    path('my_experience/',my_views.experience,name='experience'),
    path('my_educations/',my_views.education,name='education'),
    path('my_certificate/',my_views.certifications,name='certifications'),
    #################################################################################
    path('my_contact/',my_views.contact,name='contact'),
    ##############################################################
    path('my_resume/',my_views.resume, name='resume'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)