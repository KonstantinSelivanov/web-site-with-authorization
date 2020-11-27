from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    """
    A handler for the ImageCreateForm to which an authorized user has access.
    The handler receives the initial data and creates a form object. The data
    (url, title) of the image from a third-party site is filled with JS.
    The picture has its owner, who uploaded it to the site. The image object
    is saved to the database. A URL is generated for each picture.

    Обработчик для формы ImageCreateForm доступ к которой имеет авторизованный
    пользователь. Обработчик получает начальные данные и создает объект формы.
    Данные (url, title) картинки со стороннего сайта заполняются с помощью JS.
    У картинке есть свой владелец то кто ее загрузил на сайт. Объект image
    сохраняется в БД. Для каждой картики формируется URL.
    """
    if request.method == 'POST':
        image_form = ImageCreateForm(data=request.POST)
        if image_form.is_valid():
            cd = image_form.cleaned_data
            new_item = image_form.save(commit=False)
            # Adding a user to the created object
            # Добавление пользователя к созданному объекту
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Изображение успешно добавлено')
            # Redirect the user to the saved image page
            # Перенаправление пользователя на страницу сохраненного изображения
            return redirect(new_item.get_absolute_url())
        else:
            print('Ошибка, форма не валидна')
    else:
        # Filling out a form from a GET request
        # Заполнение формы из GET-запроса
        image_form = ImageCreateForm(data=request.GET)

    return render(request,
                  'images/image/create.html',
                  {'section': 'images', 'image_form': image_form})
