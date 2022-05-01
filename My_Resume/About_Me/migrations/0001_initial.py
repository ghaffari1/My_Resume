# Generated by Django 3.1.14 on 2022-05-01 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='Images/Me', verbose_name='Image Me')),
                ('Full_Name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('Age', models.IntegerField(verbose_name='Age')),
                ('Date_Of_Birth', models.CharField(max_length=50, null=True, verbose_name='Date Of Birth')),
                ('Address', models.CharField(max_length=100, verbose_name='Address')),
                ('Degree', models.CharField(max_length=50, null=True, verbose_name='Degree')),
                ('Freelance', models.CharField(max_length=50, null=True, verbose_name='Freelance')),
                ('Short_About_Me', models.CharField(max_length=50, verbose_name='Short About Me')),
                ('About_Me', models.TextField(verbose_name='About Me')),
                ('HappyClients', models.IntegerField(null=True, verbose_name='Happy Clients')),
                ('Projects', models.IntegerField(null=True, verbose_name='Projects')),
                ('HoursOfSupport', models.IntegerField(null=True, verbose_name='Hours Of Support')),
                ('Awards', models.IntegerField(null=True, verbose_name='Awards')),
                ('Instagram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Instagram')),
                ('GitHub', models.CharField(blank=True, max_length=50, null=True, verbose_name='Github')),
                ('Phone', models.CharField(max_length=13, verbose_name='Phone')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Web_Site', models.CharField(max_length=100, verbose_name='Web Site')),
                ('Is_Active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'About Me',
                'verbose_name_plural': 'About Me',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
                ('Comment', models.TextField(max_length=100, verbose_name='Comment')),
                ('Is_Active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50, verbose_name='Full Name')),
                ('EmailAddress', models.EmailField(max_length=254, verbose_name='EmailAddress')),
                ('Subject', models.CharField(max_length=50, null=True, verbose_name='Subject')),
                ('Message', models.TextField(verbose_name='Message')),
                ('Is_Read_Admin', models.BooleanField(default=False, verbose_name='Is_Read_Admin')),
            ],
            options={
                'verbose_name': 'Contact us',
                'verbose_name_plural': 'Contact us',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Majors', models.CharField(max_length=50, verbose_name='Majors')),
                ('Educational_Degree', models.CharField(max_length=50, verbose_name='Educational Degree')),
                ('Comment', models.TextField(max_length=307, verbose_name='Comment')),
                ('CreateTime', models.CharField(max_length=10, verbose_name='CreateTime')),
                ('Address', models.CharField(max_length=50, null=True, verbose_name='Address')),
                ('Is_Active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='I_Do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Images/I_Do', verbose_name='Image')),
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
                ('Comment', models.TextField(max_length=307, verbose_name='Comment')),
                ('Is_Active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'Things I can do.',
            },
        ),
        migrations.CreateModel(
            name='JobTitles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'JobTitle',
                'verbose_name_plural': 'JobTitles',
            },
        ),
        migrations.CreateModel(
            name='WorkSamples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
                ('I_Do', models.CharField(blank=True, max_length=50, null=True, verbose_name='I_Do')),
                ('Is_Active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'WorkSample',
                'verbose_name_plural': 'WorkSamples',
            },
        ),
        migrations.CreateModel(
            name='WorkSampelsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='Title Image')),
                ('Image', models.ImageField(upload_to='Images/WorkSample/', verbose_name='Image')),
                ('Is_Active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('WorkSamples', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='About_Me.worksamples', verbose_name='Images')),
            ],
            options={
                'verbose_name': 'WorkSampelsImage',
                'verbose_name_plural': 'WorkSampelsImages',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='Title')),
                ('Number', models.IntegerField(verbose_name='Percent')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Images/Skills', verbose_name='Photo of the document')),
                ('Is_Active', models.BooleanField(default=False, null=True, verbose_name='Is Active')),
                ('About_Me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='About_Me.aboutmemodel', verbose_name='Skills')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=50, verbose_name='Company Name')),
                ('Work', models.CharField(max_length=50, verbose_name='Work')),
                ('Date', models.CharField(max_length=10, verbose_name='Date')),
                ('Is_Active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('Comment', models.ManyToManyField(to='About_Me.Comment', verbose_name='Comments')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='CommentsOfOthersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(null=True, upload_to='Images/Comment/', verbose_name='Image')),
                ('FullName', models.CharField(max_length=50, verbose_name='Full Name')),
                ('Comments', models.TextField(max_length=307, verbose_name='Comments')),
                ('Job', models.CharField(blank=True, max_length=50, null=True, verbose_name='Job')),
                ('Is_Read', models.BooleanField(default=False, verbose_name='Is Read')),
                ('Comments_Of_Others', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='About_Me.aboutmemodel', verbose_name='Comments Of Others')),
            ],
            options={
                'verbose_name': 'CommentAboutMe',
                'verbose_name_plural': 'CommentsAboutMe',
            },
        ),
        migrations.AddField(
            model_name='aboutmemodel',
            name='Education',
            field=models.ManyToManyField(to='About_Me.Education', verbose_name='Education'),
        ),
        migrations.AddField(
            model_name='aboutmemodel',
            name='Experiences',
            field=models.ManyToManyField(to='About_Me.Experiences', verbose_name='Experiences'),
        ),
        migrations.AddField(
            model_name='aboutmemodel',
            name='I_do',
            field=models.ManyToManyField(to='About_Me.I_Do', verbose_name='I do'),
        ),
        migrations.AddField(
            model_name='aboutmemodel',
            name='Job_Titles',
            field=models.ManyToManyField(to='About_Me.JobTitles', verbose_name='Job Titles'),
        ),
        migrations.AddField(
            model_name='aboutmemodel',
            name='Work_Samples',
            field=models.ManyToManyField(to='About_Me.WorkSamples', verbose_name='Work Samples'),
        ),
    ]
