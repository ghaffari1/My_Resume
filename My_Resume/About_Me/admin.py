from django.contrib import admin
from About_Me.models import AboutMeModel, CommentsOfOthersModel, I_Do, Education, Experiences, WorkSamples, \
    WorkSampelsImages, ContactModel, JobTitles, Comment,Skills

# Register your models here.

admin.site.register(AboutMeModel)
admin.site.register(Skills)
admin.site.register(CommentsOfOthersModel)
admin.site.register(I_Do)
admin.site.register(Education)
admin.site.register(Experiences)
admin.site.register(WorkSamples)
admin.site.register(WorkSampelsImages)
admin.site.register(ContactModel)
admin.site.register(JobTitles)
admin.site.register(Comment)
