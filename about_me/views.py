from django.shortcuts import render
from django.views.generic import(TemplateView)
# Create your views here.
def index(request):
    return render(request,'about_me/index.html')
