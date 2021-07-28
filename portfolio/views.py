# Create your views here.
from django.shortcuts import render,redirect
from portfolio.settings.base import Email_from_to
from django.core.mail import send_mail

from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from .forms import UploadDesc, Certificate, ContactForm, Projects, Skills, About, Education, Experiene

from modelapp.models import AddDesc, AboutMe, CertificateM,ExperienceM,EducationM,ProjectsM,SkillsM,IntouchM

def index(request):
    return render(request, 'index.html')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
# Add DESC START ..................

class AddDescription(CreateView):
    form_class = UploadDesc
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateDescription(UpdateView):
    queryset = AddDesc.objects.all()
    form_class = UploadDesc
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteDescription(DeleteView):
    template_name = "delete_confirm.html"
    model = AddDesc
    success_url = '/'

# END ........................

# ABout Start ..................

class AddAbout(CreateView):
    form_class = About
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateAbout(UpdateView):
    queryset = AboutMe.objects.all()
    form_class = About
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteAbout(DeleteView):
    template_name = "delete_confirm.html"
    model = AboutMe
    success_url = '/'

# End ...............................

# Experience ..................

class AddExperience(CreateView):
    form_class = Experiene
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateExperience(UpdateView):
    queryset = ExperienceM.objects.all()
    form_class = Experiene
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteExperience(DeleteView):
    template_name = "delete_confirm.html"
    model = ExperienceM
    success_url = '/'

# END ...................

# Education ....................

class AddEducation(CreateView):
    form_class = Education
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateEducation(UpdateView):
    queryset = EducationM.objects.all()
    form_class = Education
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteEducation(DeleteView):
    template_name = "delete_confirm.html"
    model = EducationM
    success_url = '/'

# END ....................

# Certificate ............................

class AddCertificate(CreateView):
    form_class = Certificate
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateCertificate(UpdateView):
    queryset = CertificateM.objects.all()
    form_class = Certificate
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteCertificate(DeleteView):
    template_name = "delete_confirm.html"
    model = CertificateM
    success_url = '/'

# END ........................

# Skills .........................

class AddSkills(CreateView):
    form_class = Skills
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateSkills(UpdateView):
    queryset = SkillsM.objects.all()
    form_class = Skills
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteSkills(DeleteView):
    template_name = "delete_confirm.html"
    model = SkillsM
    success_url = '/'

# END .....................

# Projects ....................

class AddProjects(CreateView):
    form_class = Projects
    template_name = 'create_desc.html'
    success_url = '/'


class UpdateProjects(UpdateView):
    queryset = ProjectsM.objects.all()
    form_class = Projects
    template_name = 'create_desc.html'
    success_url = '/'


class DeleteProjects(DeleteView):
    template_name = "delete_confirm.html"
    model = ProjectsM
    success_url = '/'

# END ........................
class MainView(ListView):
    template_name = "index.html"
    context_object_name = 'data'
    queryset = AddDesc.objects.all()
    form_class = ContactForm

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message = 'From - '+name+'\nEmail Address - '+email+'\n\n'+message
            send_mail(
                subject,
                message,
                Email_from_to,
                [Email_from_to],
            )
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['aboutme'] = AboutMe.objects.all()
        context['experience'] = ExperienceM.objects.order_by('-pk')
        context['education'] = EducationM.objects.order_by('-pk')
        context['certificate'] = CertificateM.objects.order_by('-pk')
        context['skills'] = SkillsM.objects.order_by('-stars')
        context['projects'] = ProjectsM.objects.order_by('-pk')
        context['contacts'] = ContactForm
        return context