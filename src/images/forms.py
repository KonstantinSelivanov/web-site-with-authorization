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
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.URLInput, }


    def clean_url(self):
        """
        Validation of form fields. Check that the URL entered is correct:
        the file name ends with .jpg or .jpeg.
        Валидация полей формы. Проверка того, что введенный URL является
        корректным: имя файла заканчивается на .jpg или .jpeg.
        """
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Указанный URL не содержит файлов'
                                        'с расширением .jpg и .jpeg')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        """
        The overridden standard save () function of the ModelForm class
        to save a model object to the database.
        Переопределенная стандартная функция save() класса ModelForm
        для сохранения объекта модели в базу данных.
        """
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(
            slugify(image.title), image_url.rsplit('.', 1)[1].lower())
        # Download the image to the given URL
        # Скачиваем картинку по указанному адресу
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image
