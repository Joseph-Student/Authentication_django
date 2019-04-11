from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django_registration.backends.activation.views import RegistrationView, ActivationView

from accounts.forms import CustomAuthenticationForm
from accounts.forms import RegistrationForm, CustomPasswordResetForm, PasswordResetConfirmForm, \
    CustomPasswordChangeForm, CustomerUserChangeForm
from accounts.models import CustomerUser


class LoginView(auth_views.LoginView):
    template_name = 'accounts/registration/login.html'
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm


class RegisterView(RegistrationView):
    email_body_template = 'accounts/registration/activation_email_body.html'
    html_email_template_name = 'accounts/registration/activation_email_body.html'
    email_subject_template = 'accounts/registration/activation_email_subject.txt'
    success_url = reverse_lazy('accounts:register-complete')
    disallowed_url = reverse_lazy('accounts:django_registration_disallowed')
    template_name = 'accounts/registration/register_form.html'
    form_class = RegistrationForm


class ActivateAccountView(ActivationView):
    success_url = reverse_lazy('accounts:activate-complete')
    template_name = 'accounts/registration/activation_failed.html'


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'accounts/registration/password_reset_email.html'
    html_email_template_name = 'accounts/registration/password_reset_email.html'
    template_name = 'accounts/registration/password_reset_form.html'
    success_url = reverse_lazy('accounts:password-reset-done')
    form_class = CustomPasswordResetForm


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/registration/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/registration/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password-reset-complete')
    form_class = PasswordResetConfirmForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/registration/password_reset_complete.html'


class CustomUserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user/_detail.html'
    model = CustomerUser


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user/_form.html'
    model = CustomerUser
    form_class = CustomerUserChangeForm


class PasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/user/password_change.html'
    success_url = reverse_lazy('accounts:password-change-done')
    form_class = CustomPasswordChangeForm


class PasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'accounts/user/password_change_done.html'
