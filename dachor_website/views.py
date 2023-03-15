from django.views.generic import TemplateView


class NavbarHighlightMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.navbar_active] = 'active'
        return context


class HomepageView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_website/homepage.html'
    navbar_active = 'homepage'


class AboutView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_website/about.html'
    navbar_active = 'about'


class ContactView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_website/contact.html'
    navbar_active = 'contact'


class EventsView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_website/events.html'
    navbar_active = 'events'


class PrivacyView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_website/privacy.html'
    navbar_active = 'privacy'
