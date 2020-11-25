from django import forms

from .models import Image


class ImageCreateForm(forms.ModelForm):
    """
    A form for saving a picture object located on another site.
    The user will need to provide the URL of the image, its title,
    and an optional description. Our application will download
    the image and create an Image object in the database.
    Форма для сохранения объекта картинки находящейся на другом сайте.
    Пользователю нужно будет указать URL картинки, ее заголовок и
    необязательное описание. Наше приложение скачает изображение и создаст
    объект Image в базе данных.
    """
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput, }


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
