from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from dachor_internal.forms import SignupForm
from dachor_website.views import NavbarHighlightMixin


class StartView(NavbarHighlightMixin, LoginRequiredMixin, TemplateView):
    template_name = 'dachor_internal/index.html'
    navbar_active = 'internal'


class NotConfirmedView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_internal/not_confirmed.html'
    navbar_active = 'internal'


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'dachor_internal/signup.html'
    success_url = reverse_lazy('internal:not-confirmed')

