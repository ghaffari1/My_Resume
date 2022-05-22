from django.shortcuts import render
from django.views.generic import ListView

from About_Me.models import AboutMeModel, CommentsOfOthersModel, WorkSamples, Experiences, \
    ContactModel


# Create your views here.

class AboutMeView(ListView):
    template_name = 'Home-Page/index.html'
    model = AboutMeModel

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data()

        context['about_me'] = AboutMeModel.objects.filter(Is_Active=True).prefetch_related(
            'skills_set', 'worksamples_set').first()
        context['comments'] = CommentsOfOthersModel.objects.filter(Is_Read=True).prefetch_related(
            'Comments_Of_Others__commentsofothersmodel_set')

        context['Experiences'] = Experiences.objects.filter(Is_Active=True)
        return context


def Add_Message(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    subject = request.GET.get('subject')
    message = request.GET.get('message')

    # Because I do not know JavaScript, I did this.
    if email == '':
        return render(request, 'Email_Null.html', {})
    elif email[0] == '@' or email[-1] == '@' or email[0] == '.' or email[-1] == '.':
        return render(request, 'Email_Error.html', {})
    elif '.' not in email and '@' not in email:
        return render(request, 'Email_Error.html', {})
    elif len(email) <= 4:
        return render(request, 'Email_Error.html', {})
    if len(message) > 500:
        return render(request, 'Message_Error.html', {})
    elif message == '':
        return render(request, 'Message_Null.html', {})
    if len(name) > 50:
        return render(request, 'Name_Error.html', {})
    elif name == '':
        return render(request, 'Name_Null.html', {})
    ####################################################
    new_message = ContactModel(FullName=name, EmailAddress=email, Subject=subject, Message=message)
    new_message.save()
    return render(request, 'Comment_Result.html', {})
