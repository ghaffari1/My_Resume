from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Education(models.Model):
    Majors = models.CharField(max_length=50, verbose_name='Majors')
    Educational_Degree = models.CharField(max_length=50, verbose_name='Educational Degree')
    Comment = models.TextField(max_length=307, verbose_name='Comment')
    CreateTime = models.CharField(max_length=10, verbose_name='CreateTime')
    Address = models.CharField(max_length=50, null=True, verbose_name='Address')
    Is_Active = models.BooleanField(default=False, verbose_name='Is Active')

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.Educational_Degree


class Comment(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')
    Comment = models.TextField(max_length=100, verbose_name='Comment')
    Is_Active = models.BooleanField(default=False, verbose_name='Is Active')

    class Meta:
        verbose_name = 'Comment for Experience'
        verbose_name_plural = 'Comments for Experience'

    def __str__(self):
        return self.Title


class Experiences(models.Model):
    Company_Name = models.CharField(max_length=50, verbose_name='Company Name')
    Work = models.CharField(max_length=50, verbose_name='Work')
    Comment = models.ManyToManyField(to=Comment, verbose_name='Comments')
    Date = models.CharField(max_length=10, verbose_name='Date')
    Is_Active = models.BooleanField(default=False, verbose_name='Is Active')

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.Company_Name


class JobTitles(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')

    class Meta:
        verbose_name = 'JobTitle'
        verbose_name_plural = 'JobTitles'

    def __str__(self):
        return self.Title


class AboutMeModel(models.Model):
    # InfoMe #
    Image = models.ImageField(upload_to='Images/Me', null=True, verbose_name='Image Me')
    Full_Name = models.CharField(max_length=50, verbose_name='Full Name')
    Age = models.IntegerField(verbose_name='Age')
    Date_Of_Birth = models.CharField(max_length=50, null=True, verbose_name='Date Of Birth')
    Address = models.CharField(max_length=100, verbose_name='Address')
    Degree = models.CharField(max_length=50, null=True, verbose_name='Degree')
    Freelance = models.CharField(max_length=50, null=True, verbose_name='Freelance')
    Short_About_Me = models.CharField(max_length=50, verbose_name='Short About Me')
    About_Me = models.TextField(verbose_name='About Me')
    # JobTitle #
    Job_Titles = models.ManyToManyField(to=JobTitles, verbose_name='Job Titles')
    # Education #
    Education = models.ManyToManyField(to=Education, verbose_name='Education')
    # Experiences #
    Experiences = models.ManyToManyField(to=Experiences, verbose_name='Experiences')

    # Facts #
    HappyClients = models.IntegerField(null=True, verbose_name='Happy Clients')
    Projects = models.IntegerField(null=True, verbose_name='Projects')
    HoursOfSupport = models.IntegerField(null=True, verbose_name='Hours Of Support')
    Awards = models.IntegerField(null=True, verbose_name='Awards')
    # Contact #
    Instagram = models.CharField(max_length=50, null=True, blank=True, verbose_name='Instagram')
    GitHub = models.CharField(max_length=50, null=True, blank=True, verbose_name='Github')
    Phone = models.CharField(max_length=13, verbose_name='Phone')
    Email = models.EmailField(verbose_name='Email')
    Web_Site = models.CharField(max_length=100, verbose_name='Web Site')
    # IsActive #
    Is_Active = models.BooleanField(default=False, verbose_name='Is Active', unique=True)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.Full_Name


class Skills(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Title')
    Number = models.IntegerField(verbose_name='Percent')
    Image = models.ImageField(upload_to='Images/Skills', null=True, blank=True, verbose_name='Photo of the certificate')
    Link = models.CharField(max_length=200, null=True,blank=True, verbose_name='Link')
    AboutMe = AboutMeModel.objects.filter(Is_Active=True).first()
    about_me = models.ForeignKey(to=AboutMeModel, default=AboutMe.id, on_delete=models.CASCADE,
                                 null=True,
                                 verbose_name='About_me', editable=False)
    Is_Active = models.BooleanField(default=False, null=True, verbose_name='Is Active')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.Title

class WorkSamples(models.Model):
    Image = models.ImageField(upload_to='Images/WorkSample/', verbose_name='Image')
    Title = models.CharField(max_length=50, verbose_name='Title')
    I_Do = models.CharField(max_length=50, verbose_name='I_Do')
    Link = models.CharField(max_length=100, null=True, blank=True, verbose_name='Link')
    WorkSampleImage = models.ForeignKey(to=AboutMeModel, on_delete=models.CASCADE,
                                        verbose_name='About us', editable=False,
                                        default=AboutMeModel.objects.filter(Is_Active=True).first().id)
    Is_Active = models.BooleanField(default=True, verbose_name='Is Active')

    class Meta:
        verbose_name = 'WorkSample'
        verbose_name_plural = 'WorkSamples'

    def __str__(self):
        return self.Title


class CommentsOfOthersModel(models.Model):
    Image = models.ImageField(null=True, upload_to='Images/Comment/', verbose_name='Image')
    FullName = models.CharField(max_length=50, verbose_name='Full Name')
    Comments = models.TextField(max_length=307, verbose_name='Comments')
    Job = models.CharField(max_length=50, null=True, blank=True, verbose_name='Job')
    Is_Read = models.BooleanField(default=False, verbose_name='Is Read')
    AboutMe = AboutMeModel.objects.filter(Is_Active=True).first()
    Comments_Of_Others = models.ForeignKey(to=AboutMeModel, default=AboutMe.id, on_delete=models.CASCADE,
                                           null=True,
                                           verbose_name='Comments Of Others', editable=False)

    class Meta:
        verbose_name = 'CommentAboutMe'
        verbose_name_plural = 'CommentsAboutMe'

    def __str__(self):
        return self.FullName


class ContactModel(models.Model):
    FullName = models.CharField(max_length=50, verbose_name='Full Name')
    EmailAddress = models.EmailField(verbose_name='EmailAddress')
    Subject = models.CharField(max_length=50, null=True, verbose_name='Subject')
    Message = models.TextField(max_length=500, verbose_name='Message')
    Is_Read_Admin = models.BooleanField(default=False, verbose_name='Is_Read_Admin')

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

    def __str__(self):
        return self.FullName
