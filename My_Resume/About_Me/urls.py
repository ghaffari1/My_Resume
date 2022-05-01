from django.urls import path

from About_Me.views import AboutMeView

urlpatterns = [
    path('', AboutMeView.as_view(), name='AboutMeUrl'),
]
