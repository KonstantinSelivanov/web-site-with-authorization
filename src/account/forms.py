from django import forms


class LoginForm(form.Form):
    """ User authorization form """
    """ Форма авторизации пользователя """

    username = forms.CharField(verbose_name='Имя пользователя', max_length=30)
    password = forms.CharField(verbose_name='Пароль',
                               min_length=8,
                               widget=forms.PasswordInput)
