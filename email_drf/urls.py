from django.urls import path
from email_drf.views import EmailView

urlpatterns = [
    path("send_email/", EmailView.as_view()),
]
