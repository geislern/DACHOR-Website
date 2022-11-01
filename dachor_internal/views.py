from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from dachor_website.views import NavbarHighlightMixin


class StartView(NavbarHighlightMixin, LoginRequiredMixin, TemplateView):
    template_name = 'dachor_internal/index.html'
    navbar_active = 'internal'

