from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import LoginForm


def user_authorization(request):
    """
    User authorization web service.
    Tasks:
        - getting username and password from the form;
        - verification of data with those contained in the database;
        - user authorization and session creation.

    """

    """
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
            print(user)
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
