from django.urls import path

from About_Me.views import AboutMeView, Add_Message

urlpatterns = [
    path('', AboutMeView.as_view(), name='AboutMeUrl'),
    path('add-message/', Add_Message, name='add-message'),
]
