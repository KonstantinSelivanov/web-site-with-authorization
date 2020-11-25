from django.contrib import messages
from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """
    User authentication by e-mail
    Аутентификация пользователя по e-mail
    """

    def authenticate(self, request, username=None, password=None):
        """
        The method is used to get the user corresponding to the specified email
        and password using the check_password () method of the user model.
        This method encrypts the password and compares the result with
        the one stored in the database
        Метод служит для получения пользователя, соответствующего указанным
        электронной почте и паролю, с помощью метода check_password()
        модели пользователя. Этот метод выполняет шифрование пароля и
        сравнивает результат с тем, который хранится в базе данных
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        The method is used to get a user by ID
        Метод служит  для получения пользователя по ID
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
