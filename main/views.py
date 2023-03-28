from django.views import generic
from main.forms import ContactForm
from main.models import Contact
from servise import send


class ContactView(generic.CreateView):
    """Displaying the email subscription form"""

    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "main/contact.html"

    def form_valid(self, form: ContactForm) -> None:
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
