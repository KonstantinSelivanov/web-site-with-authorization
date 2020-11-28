from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from urllib import request

from .models import Image


class ImageCreateForm(forms.ModelForm):
    """
    A form for saving a picture object located on another site.
    The user will need to provide the URL of the image, its title,
    and an optional description. Our application will download
    the image and create an Image object in the database.
    Форма для сохранения объекта изображения находящегося на другом сайте.
    Пользователю нужно будет указать URL изображения, ее заголовок и
    необязательное описание. Наше приложение скачает изображение и создаст
    объект Image в базе данных.
    """
    class Meta:
        model = Image
        fields = ('title', 'image', 'description')
