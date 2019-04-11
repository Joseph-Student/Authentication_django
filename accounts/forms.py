from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm,\
    ReadOnlyPasswordHashField, UsernameField
from django.urls import reverse_lazy
from django_registration.forms import RegistrationForm as BaseRegistrationForm

from accounts.models import CustomerUser


class BaseBootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseBootstrapForm, self).__init__(*args, **kwargs)

        for name, value in self.fields.items():
            if not isinstance(value.widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple)):
                value.widget.attrs.setdefault('class', 'form-control')
                value.widget.attrs.setdefault('placeholder', value.label)


class CustomAuthenticationForm(BaseBootstrapForm, AuthenticationForm):
    pass


class RegistrationForm(BaseBootstrapForm, BaseRegistrationForm):
    pass


class CustomPasswordResetForm(BaseBootstrapForm, PasswordResetForm):
    pass


class PasswordResetConfirmForm(BaseBootstrapForm, SetPasswordForm):
    pass


class CustomPasswordChangeForm(BaseBootstrapForm, PasswordChangeForm):
    pass


class CustomerUserChangeForm(BaseBootstrapForm, forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label='Contraseña',
        help_text="Las contraseñas sin procesar no se almacenan, por lo que no "
                  "hay forma de ver la contraseña de este usuario, pero puedes cambiar "
                  "la contraseña usando <a href=\"{}\">este formulario</a>."
    )

    class Meta:
        model = CustomerUser
        fields = ('password', 'username', 'email', 'first_name', 'last_name')
        field_classes = {'username': UsernameField}
        widgets = {
            'username': forms.TextInput(attrs={'readonly': True}),
            'email': forms.TextInput(attrs={'readonly': True})
        }

    def __init__(self, *args, **kwargs):
        super(CustomerUserChangeForm, self).__init__(*args, **kwargs)
        password = self.fields.get('password')

        if password:
            password.help_text = password.help_text.format(reverse_lazy('accounts:password-change'))

    def clean_password(self):
        return self.initial.get('password')
