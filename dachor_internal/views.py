from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView

from dachor_internal.forms import SignupForm, ProfileForm
from dachor_website.views import NavbarHighlightMixin


class StartView(NavbarHighlightMixin, LoginRequiredMixin, TemplateView):
    template_name = 'dachor_internal/index.html'
    navbar_active = 'internal'


class NotConfirmedView(NavbarHighlightMixin, TemplateView):
    template_name = 'dachor_internal/not_confirmed.html'
    navbar_active = 'internal'


class SignupView(NavbarHighlightMixin, CreateView):
    form_class = SignupForm
    template_name = 'dachor_internal/signup.html'
    success_url = reverse_lazy('internal:not-confirmed')
    navbar_active = 'internal'


class ProfileEditView(NavbarHighlightMixin, FormView):
    form_class = ProfileForm
    template_name = 'dachor_internal/edit_profile.html'
    success_url = reverse_lazy('internal:profile-edit')
    navbar_active = 'internal'

    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs.update(instance=self.request.user.profile)
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Informationen aktualisiert")
        return super().form_valid(form)
