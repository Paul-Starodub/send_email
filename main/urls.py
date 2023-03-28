from django.urls import path
from main.views import ContactView

urlpatterns = [path("", ContactView.as_view(), name="contact")]


app_name = "email"
