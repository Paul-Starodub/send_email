from django.core.mail import send_mail
from send_email.celery import app
from .models import Contact

from .servise import send


@app.task
def send_spam_email(user_email: str) -> None:
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            "We will send you spam",
            "Very active spam every 2 min",
            "allex@gmail.com",
            [contact.email],
            fail_silently=False,
        )
