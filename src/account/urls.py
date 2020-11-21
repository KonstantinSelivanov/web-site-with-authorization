from django.urls import path

from . import views


urlpatterns = [
    # Previous login view
    # Предыдущая авторизация
    path('login/', views.user_authorization, name='login'),
]
