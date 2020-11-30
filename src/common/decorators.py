from django.http import HttpResponseBadRequest


def ajax_required(f):
    """
    A decorator for AJAX handlers so that they can only accept AJAX requests.
    The Django request object has an is_ajax() method that checks
    if the request was made using XMLHttpRequest. This means that it is
    asynchronous.
    Декоратор для AJAX-обработчиков, чтобы они могли принимать только
    AJAX-запросы. У объекта запроса Django есть метод is_ajax(), который
    проверяет, сделан ли запрос с помощью XMLHttpRequest. Это означает, что он
    является асинхронным.
    """
    def wrap(request, *args, **kwargs):
        """
        A function that returns an HttpResponseBadRequest object
        (error code 400) if the request is not an AJAX request.
        Otherwise, the result of executing the decorated function is returned.
        Функция которая возвращает объект HttpResponseBadRequest
        (код ошибки – 400), если запрос не является AJAX-запросом. В противном
        случае возвращается результат выполнения декорируемой функции.
        """
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
