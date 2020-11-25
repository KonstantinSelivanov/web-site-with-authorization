from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    """
    Model for saving pictures and related information
    Модель для сохранения картинок и связанной с ними информации
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(verbose_name='URL')
    image = models.ImageField(verbose_name='Картинка',
                              upload_to='image/%Y/%m/%d')
    description = models.TextField(verbose_name='Описание',
                                   max_length=450,
                                   blank=True)
    created = models.DateTimeField(verbose_name='Дата и время создания',
                                   auto_now_add=True,
                                   db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)
    user_dislike = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                          related_name='images_disliked',
                                          blank=True)

    class Meta:
        verbose_name = 'Картику'
        verbose_name_plural = 'Картинка'

    def _str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Overridden standard save() function. Serves for automatic slug
        creation. If the image has no slug, the slugify() function
        automatically forms it from the passed header, after which
        the image object is saved.
        Переопределенная стандартная функция save(). Служит для автоматического
        формирования slug. Если у изображения нет слага, функция slugify()
        автоматически формирует его из переданного заголовка, после чего
        происходит сохранение объекта картинки.
        """

        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
