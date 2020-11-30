from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, request
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ImageCreateForm
from .models import Image
from common.decorators import ajax_required


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
    """ Handler for viewing and editing image information """
    """ Обработчик для просмотра и редактирования сведений об изображениях"""
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',
                           {'section': 'images', 'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    """
    Decorator ajax_required so the handler can only accept AJAX requests.
    The login_required decorator prevents unauthorized users from accessing
    this handler. The require_POST decorator returns an HttpResponseNotAllowed
    error (response status 405) if the request was not POSTed. The handler will
    only be executed for POST requests.

    A handler for liking and unmarking images.

    Декоратор ajax_required чтобы обработчик мог принимать только AJAX-запросы.
    Декоратор login_required не дает неавторизованным пользователям доступ к
    этому обработчику. Декоратор require_POST возвращает ошибку
    HttpResponseNotAllowed (статус ответа 405), если запрос отправлен
    не методом POST. Обработчик будет выполняться только при POST-запросах.

    Обработчик для отметки изображения как понравившиеся и снимать эту отметку.
    """
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


@login_required
def image_list(request):
    """
    Handler for displaying a list of images. The handler will handle
    the standard page load and AJAX request to get the next 8 images.
    Обработчик для отображения списка изображений.
    Обработчик будет обрабатывать стандартную загрузку страницы и AJAX-запрос
    для получения следующих 8 изображений.
    """
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If the front page is not a number, return the first.
        # Если передняя страница не является числом, возвращаем первую.
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If we receive an AJAX request with a page number greater
            # than their number, we return an empty page.
            # Если получили AJAX-запрос с номером страницы, большим,
            # чем их количество, возвращаем пустую страницу.
            return HttpResponse('')
        # If the page number is greater than their number, return the last one.
        # Если номер страницы больше, чем их количество, возвращаем последнюю.
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'images/image/list_ajax.html',
                               {'section': 'images', 'images': images})
    return render(request, 'images/image/list.html',
                           {'section': 'images', 'images': images})
