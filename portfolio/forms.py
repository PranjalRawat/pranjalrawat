from django import forms
from modelapp.models import AddDesc, AboutMe, CertificateM, ExperienceM, EducationM, ProjectsM, SkillsM

class UploadDesc(forms.ModelForm):
    class Meta:
        model = AddDesc
        fields = [
            "field",
            'profile',
            "title1",
            "titleLink1",
            "title2",
            "titleLink2",
            "title3",
            "titleLink3",
            "title4",
            "titleLink4",
            "title5",
            "titleLink5",
            "title6",
            "titleLink6",
        ]

class About(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = [
            "description",
            "resume",
            "address"
        ]

class Experiene(forms.ModelForm):
    class Meta:
        model = ExperienceM
        fields = [
            "company",
            "designation",
            "duration",
            "desc"
        ]

class Education(forms.ModelForm):
    class Meta:
        model = EducationM
        fields = [
            "institute",
            "course",
            "duration",
            "detail",
            "icon"
        ]

class Skills(forms.ModelForm):
    class Meta:
        model = SkillsM
        fields = [
            "topic",
            "cover_img",
            "level",
            "stars",
            "bg_color"
        ]


class Certificate(forms.ModelForm):
    class Meta:
        model = CertificateM
        fields = [
            "course",
            "detail",
            'source',
            "link",
            "badge",
            "badgeLink"
        ]


class Projects(forms.ModelForm):
    class Meta:
        model = ProjectsM
        fields = [
            "title",
            "image",
            "description",
            "link",
        ]


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    