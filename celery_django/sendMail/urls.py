from django.urls import path
from . import views
urlpatterns = [
    path('sendmail/',views.send_mail,name='sendmail'),
]
