from django.db import models


class AddDesc(models.Model):
    description = models.TextField()
    title1 = models.CharField(max_length=140)
    titleLink1 = models.CharField(max_length=240)
    title2 = models.CharField(max_length=140)
    titleLink2 = models.CharField(max_length=240)
    title3 = models.CharField(max_length=140)
    titleLink3 = models.CharField(max_length=240)
    title4 = models.CharField(max_length=140)
    titleLink4 = models.CharField(max_length=240)
    title5 = models.CharField(max_length=140)
    titleLink5 = models.CharField(max_length=240)
    title6 = models.CharField(max_length=140)
    titleLink6 = models.CharField(max_length=240)

    def __str__(self):
        return str(self.title)


class AboutMe(models.Model):
    description = models.TextField()
    profile = models.ImageField(upload_to='profile_pic/')
    resume = models.FileField()
    address = models.TextField()


class EducationM(models.Model):
    institute = models.CharField(max_length=240)
    course = models.CharField(max_length=240)
    duration = models.CharField(max_length=240)
    detail = models.TextField()


class CertificateM(models.Model):
    course = models.CharField(max_length=240)
    detail = models.TextField()
    link = models.CharField(max_length=240)
    badge = models.ImageField(upload_to='badges/')
    badgeLink = models.CharField(max_length=240, default=None)


class SkillsM(models.Model):
    topic = models.CharField(max_length=240)
    cover_img = models.CharField(max_length=240)
    level = models.CharField(max_length=240)
    stars = models.IntegerField()
    bg_color = models.CharField(max_length=240)


class ProjectsM(models.Model):
    title = models.CharField(max_length=240)
    image = models.ImageField(upload_to="project/images/")
    link = models.CharField(max_length=240)
    description = models.TextField()
