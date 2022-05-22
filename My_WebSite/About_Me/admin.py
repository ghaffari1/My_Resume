from django.contrib import admin
from About_Me.models import AboutMeModel, CommentsOfOthersModel, Education, Experiences, WorkSamples, \
    ContactModel, JobTitles, Comment, Skills


# Register your models here.
class AdminAboutMe(admin.ModelAdmin):
    list_display = ['Full_Name', 'Is_Active']
    list_editable = ['Is_Active']


admin.site.register(AboutMeModel, AdminAboutMe)
admin.site.register(Skills)
admin.site.register(CommentsOfOthersModel)
admin.site.register(Education)
admin.site.register(Experiences)
admin.site.register(WorkSamples)
admin.site.register(ContactModel)
admin.site.register(JobTitles)
admin.site.register(Comment)