from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, request
from django.views.decorators.http import require_POST

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
        image_form = ImageCreateForm(request.POST, request.FILES)
        if image_form.is_valid():
            print(image_form.errors)
            cd = image_form.cleaned_data
            new_item = image_form.save(commit=False)
            # Adding a user to the created object
            # Добавление пользователя к созданному объекту
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Изображение успешно добавлено')
            return redirect(new_item.get_absolute_url())
        else:
            messages.error(request, image_form.errors)
    else:
        # Filling out a form from a GET request
        # Заполнение формы из GET-запроса
        image_form = ImageCreateForm(data=request.GET)

    return render(request,
                  'images/image/create.html',
                  {'section': 'images', 'image_form': image_form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',
                           {'section': 'images', 'image': image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'ok'})
