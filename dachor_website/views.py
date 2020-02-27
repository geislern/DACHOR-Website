# Create your views here.
from django.views.generic import TemplateView, RedirectView


class HomepageView(TemplateView):
    template_name = 'dachor_website/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = 'active'
        return context


class AboutView(TemplateView):
    template_name = 'dachor_website/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = 'active'
        return context


class ContactView(TemplateView):
    template_name = 'dachor_website/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = 'active'
        return context


class EventsView(TemplateView):
    template_name = 'dachor_website/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = 'active'
        return context


class LoginView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return "https://cloud.dachor-darmstadt.de/index.php/s/mQG9jq4ZsXTtzsm"


# class LoginView(TemplateView):
#    template_name = 'dachor_website/login.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['login'] = 'active'
#        return context


class PrivacyView(TemplateView):
    template_name = 'dachor_website/privacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['privacy'] = 'active'
        return context
