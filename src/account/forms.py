from django import forms
from django.contrib.auth.models import User

from .models import ProfileUser


class LoginForm(forms.Form):
    """ User authorization form """
    """ Форма авторизации пользователя """

    username = forms.CharField(label='Имя пользователя', max_length=30)
    password = forms.CharField(label='Пароль',
                               min_length=8,
                               widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """ User registration form """
    """ Форма регистрации пользователя """

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Повторите пароль',
                                            widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password_confirmation(self):
        """ The function of checking if the entered passwords match """
        """ Функция проверки совпадения введенных паролей """
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirmation']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password_confirmation']


class UserEditForm(forms.ModelForm):
    """ Form editing basic user profile information """
    """ Форма редактирования базовых данных профиля пользователя """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUserEditForm(forms.ModelForm):
    """ Form for editing additional user profile data """
    """ Форма редактирования дополнительных данных профиля пользователя """

    class Meta:
        model = ProfileUser
        fields = ('date_of_birth', 'photo')
