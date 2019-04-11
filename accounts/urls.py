from django.contrib.auth.views import logout_then_login
from django.urls import path
from django.views.generic import TemplateView

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing-page'),
    path('activate/complete/',
         TemplateView.as_view(
             template_name='accounts/registration/activation_complete.html'
         ),
         name='activate-complete'),
    path('activate/<str:activation_key>/', views.ActivateAccountView.as_view(), name='activate'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/complete/',
         TemplateView.as_view(
             template_name='accounts/registration/register_complete.html'
         ),
         name='register-complete'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password-reset-done'),

    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password-change-done'),

    path('user/<int:pk>/details/', views.CustomUserDetailView.as_view(), name='user-details'),
    path('user/<int:pk>/update/', views.CustomUserUpdateView.as_view(), name='user-update'),
]
