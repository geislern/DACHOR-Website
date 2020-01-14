# Create your views here.
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'dachor_website/homepage.html'


class AboutView(TemplateView):
    template_name = 'dachor_website/about.html'


class ContactView(TemplateView):
    template_name = 'dachor_website/contact.html'


class EventsView(TemplateView):
    template_name = 'dachor_website/events.html'


class ImpressView(TemplateView):
    template_name = 'dachor_website/impress.html'


class LoginView(TemplateView):
    template_name = 'dachor_website/login.html'


class PrivacyView(TemplateView):
    template_name = 'dachor_website/privacy.html'
