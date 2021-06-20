"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import AddAbout, AddCertificate, AddEducation, AddProjects, AddSkills, DeleteCertificate, DeleteEducation, DeleteProjects, DeleteSkills, MainView, AddDescription, UpdateAbout, UpdateCertificate, UpdateDescription, DeleteDescription, UpdateEducation, UpdateProjects, UpdateSkills

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('edit/', AddDescription.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/update/$', UpdateDescription.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$',DeleteDescription.as_view(),name='delete'),
    path('editabout/', AddAbout.as_view(), name='editabout'),
    url(r'^(?P<pk>\d+)/updateabout/$', UpdateAbout.as_view(), name='updateabout'),
    path('addeducation/', AddEducation.as_view(), name='addedu'),
    url(r'^(?P<pk>\d+)/updateeducation/$',
        UpdateEducation.as_view(), name='updateedu'),
    url(r'^(?P<pk>\d+)/deleteeducation/$',
        DeleteEducation.as_view(), name='deleteedu'),
    path('addcertificate/', AddCertificate.as_view(), name='addcertificate'),
    url(r'^(?P<pk>\d+)/updatecertificate/$',
        UpdateCertificate.as_view(), name='updatecertificate'),
    url(r'^(?P<pk>\d+)/deletecertificate/$',
        DeleteCertificate.as_view(), name='deletecertificate'),
    path('addskill/', AddSkills.as_view(), name='addskill'),
    url(r'^(?P<pk>\d+)/updateskill/$', UpdateSkills.as_view(), name='updateskill'),
    url(r'^(?P<pk>\d+)/deleteskill/$', DeleteSkills.as_view(), name='deleteskill'),
    path('addproject/', AddProjects.as_view(), name='addproject'),
    url(r'^(?P<pk>\d+)/updateproject/$',
        UpdateProjects.as_view(), name='updateproject'),
    url(r'^(?P<pk>\d+)/deleteproject/$',
        DeleteProjects.as_view(), name='deleteproject'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
