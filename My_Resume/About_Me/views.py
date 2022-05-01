from django.views.generic import CreateView
from About_Me.forms import ContactForm
from About_Me.models import AboutMeModel, CommentsOfOthersModel, I_Do, WorkSamples, WorkSampelsImages, Experiences


# Create your views here.

class AboutMeView(CreateView):
    template_name = 'Home-Page/index.html'
    form_class = ContactForm
    context_object_name = 'contact'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data()
        context['about_me'] = AboutMeModel.objects.filter(Is_Active=True).first()
        context['comments'] = CommentsOfOthersModel.objects.filter(Is_Read=True)
        context['i_do'] = I_Do.objects.all()
        context['worksamples'] = WorkSamples.objects.filter(Is_Active=True)
        context['worksamplesimage'] = WorkSampelsImages.objects.filter(Is_Active=True)
        context['Experiences'] = Experiences.objects.filter(Is_Active=True)
        return context
