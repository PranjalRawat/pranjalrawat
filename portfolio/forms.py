from django import forms
from appForModel.models import AddDesc, AboutMe, CertificateM, EducationM, ProjectsM, SkillsM


class UploadDesc(forms.ModelForm):
    class Meta:
        model = AddDesc
        fields = [
            "description",
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
            "profile",
            "resume",
            "address"
        ]


class Education(forms.ModelForm):
    class Meta:
        model = EducationM
        fields = [
            "institute",
            "course",
            "duration",
            "detail"
        ]


class Certificate(forms.ModelForm):
    class Meta:
        model = CertificateM
        fields = [
            "course",
            "detail",
            "link",
            "badge",
            "badgeLink"
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
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Name .'}), max_length=50)

    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter the subject .'}), max_length=50)

    email_address = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email Address .'}), max_length=150)

    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 40, 'placeholder': 'Enter Your Message ... '}), max_length=2000)
