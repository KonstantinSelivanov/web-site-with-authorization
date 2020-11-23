from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # Previous login view
    # Предыдущая авторизация
    # path('login/', views.user_authorization, name='login'),
    # User login template
    # Шаблон для входа пользователя на сайт
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # Template for user logout from the site
    # Шаблон для выхода пользователя с сайта
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Template dashboard
    # Шаблон рабочего стола
    path('', views.dashboard, name='dashboard'),
    # User password change template
    # Шаблон смены пароля пользователя
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # Template password recovery
    # Шаблон восстановления пароля
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # Template user registration
    # Шаблон регистрации пользователя
    path('register/', views.user_registration, name='user_registration'),
]
