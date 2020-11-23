from django.db import models
from django.conf import settings


class ProfileUser(models.Model):
    """
    User profile model. In addition to the standard User model fields,
    the following fields have been added: 'birthday' = 'date_of_birth'
    and 'photo' = 'photo'.

    Модель профиля пользователя. Помимо стандартный полей модели User
    добавлены поля: 'день рождения' = 'date_of_birth' и 'фотография' = 'photo'
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Дата рождения',
                                     blank=True,
                                     null=True)
    photo = models.ImageField(verbose_name='Фото',
                              upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)
