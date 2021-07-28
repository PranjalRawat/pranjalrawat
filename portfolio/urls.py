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
from django.conf.urls import url,include

from django.conf import settings
from django.conf.urls.static import static

from .views import AddAbout, AddCertificate, AddExperience, AddEducation, AddProjects, AddSkills, DeleteAbout, DeleteCertificate, DeleteDescription, DeleteExperience, DeleteEducation, DeleteProjects, DeleteSkills, MainView, AddDescription, UpdateAbout, UpdateCertificate, UpdateExperience, UpdateDescription, UpdateEducation, UpdateProjects, UpdateSkills

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("django.contrib.auth.urls")),
    path('', MainView.as_view(), name='index'),
    # ..........................................

    path('info/add/', AddDescription.as_view(), name='add'),
    url(r'^info/(?P<pk>\d+)/update/$', UpdateDescription.as_view(), name='update'),
    url(r'^info/(?P<pk>\d+)/delete/$',DeleteDescription.as_view(),name='delete'),

    # ..........................................

    path('info/addabout/', AddAbout.as_view(), name='addabout'),
    url(r'^info/(?P<pk>\d+)/updateabout/$', UpdateAbout.as_view(), name='updateabout'),
    url(r'^info/(?P<pk>\d+)/deleteeabout/$', DeleteAbout.as_view(), name='deleteabout'),
    # ..........................................

    path('info/addexperience/', AddExperience.as_view(), name='addexp'),
    url(r'^info/(?P<pk>\d+)/updateexperience/$',
        UpdateExperience.as_view(), name='updateexp'),
    url(r'^info/(?P<pk>\d+)/deleteexperience/$',
        DeleteExperience.as_view(), name='deleteexp'),

    # ..........................................

    path('info/addeducation/', AddEducation.as_view(), name='addedu'),
    url(r'^info/(?P<pk>\d+)/updateeducation/$',
        UpdateEducation.as_view(), name='updateedu'),
    url(r'^info/(?P<pk>\d+)/deleteeducation/$',
        DeleteEducation.as_view(), name='deleteedu'),

    # ..........................................

    path('info/addcertificate/', AddCertificate.as_view(), name='addcertificate'),
    url(r'^info/(?P<pk>\d+)/updatecertificate/$',
        UpdateCertificate.as_view(), name='updatecertificate'),
    url(r'^info/(?P<pk>\d+)/deletecertificate/$',
        DeleteCertificate.as_view(), name='deletecertificate'),

    # ..........................................

    path('info/addskill/', AddSkills.as_view(), name='addskill'),
    url(r'^info/(?P<pk>\d+)/updateskill/$', UpdateSkills.as_view(), name='updateskill'),
    url(r'^info/(?P<pk>\d+)/deleteskill/$', DeleteSkills.as_view(), name='deleteskill'),

    # ..........................................

    path('info/addproject/', AddProjects.as_view(), name='addproject'),
    url(r'^info/(?P<pk>\d+)/updateproject/$',
        UpdateProjects.as_view(), name='updateproject'),
    url(r'^info/(?P<pk>\d+)/deleteproject/$',
        DeleteProjects.as_view(), name='deleteproject'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

handler404 = "portfolio.views.page_not_found_view"