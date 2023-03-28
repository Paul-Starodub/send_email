from django.core.mail import send_mail


def send(user_email):
    send_mail(
        "We will send you spam",
        "Very active spam",
        "allex@gmail.com",
        [user_email],
        fail_silently=False,
    )
