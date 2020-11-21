from django import forms


class LoginForm(forms.Form):
    """ User authorization form """
    """ Форма авторизации пользователя """

    # Имя пользователя
    username = forms.CharField(label='Имя пользователя', max_length=30)
    # Пароль
    password = forms.CharField(label='Пароль',
                               min_length=8,
                               widget=forms.PasswordInput)
