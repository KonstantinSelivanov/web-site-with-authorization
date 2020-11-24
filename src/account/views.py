from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm
from .forms import UserEditForm, ProfileUserEditForm
from .models import ProfileUser


def user_authorization(request):
    """
    User authorization web service.
    Tasks:
        - getting username and password from the form;
        - verification of data with those contained in the database;
        - user authorization and session creation.

    Веб-сервис авторизации пользователя.
    Действия:
        - получение логина и пароля пользователя из формы;
        - сверка данных с теми, что содержаться в базе данных;
        - авторизация пользователя и создания сессии.
    """

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация успешно пройдена')
                else:
                    return HttpResponse('Учетная запись отключена')
            else:
                return HttpResponse('Неверный логин и\\или пароль')
    else:
        login_form = LoginForm()
    return render(request, 'account/login.html', {'login_form': login_form})


@login_required
def dashboard(request):
    """
    Decorator for checking if the user is authorized.
    A handler for displaying the desktop, which the user will see
    when they log into their account.
    'section' is a context variable, with the help of it we find out which
    section of the site

    Декоратор для проверки авторизован ли пользователь.
    Обработчик для отображения рабочего стола, который пользователь увидит при
    входе в свой аккаунт.
    'section ' - переменная контекста, с помощью ее узнаем какой раздел сайта
    просматривает пользователь.
    """
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def user_registration(request):
    """ User registration """
    """ Регистрация нового пользователя """
    if request.method == 'POST':
        user_registration_form = UserRegistrationForm(request.POST)
        if user_registration_form.is_valid():
            # Create a new user for now without saving to the database
            # Создание нового пользователя пока без сохранения в базе данных
            new_user = user_registration_form.save(commit=False)
            # Setting the user an encrypted password
            # Задача пользователю зашифрованного пароля
            new_user.set_password(
                user_registration_form.cleaned_data['password'])
            # Saving a user in the database
            # Сохранение пользователя в базе данных
            new_user.save()
            # Create user profile
            # Создание профиля пользователя
            ProfileUser.objects.create(user=new_user)
            return render(request, 'account/register_done.html',
                                   {'new_user': new_user})
    else:
        user_registration_form = UserRegistrationForm()
    return render(request, 'account/register.html',
                           {'user_registration_form': user_registration_form})


# Decorator for views that checks that the user is logged in, redirect to
# the log-in page if necessary.
# Декоратор для представлений, который проверяет, что пользователь вошел
# в систему, при необходимости перенаправляет на страницу входа.
@login_required
def edit_user_profile(request):
    """ Saving changes to the user profile """
    """ Сохранение изменений в профиле пользователя """
    print('1')
    if request.method == 'POST':
        print('2')
        user_edit_form = UserEditForm(instance=request.user,
                                      data=request.POST)
        profile_user_edit_form = ProfileUserEditForm(
            instance=request.user.profileuser,
            data=request.POST,
            files=request.FILES)
        if user_edit_form.is_valid() and profile_user_edit_form.is_valid():
            user_edit_form.save()
            profile_user_edit_form.save()
            messages.success(request, 'Профиль успешно обновлен')
        else:
            messages.error(request, 'Ошибка обновления вашего профиля')
    else:
        print('3')
        user_edit_form = UserEditForm(instance=request.user)
        profile_user_edit_form = ProfileUserEditForm(
            instance=request.user.profileuser)
    print('4')
    return render(request, 'account/edit_user_profile.html',
                           {'user_edit_form': user_edit_form,
                            'profile_user_edit_form': profile_user_edit_form})
