from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone


class Image(models.Model):
    """
    Model for saving images and related information
    Модель для сохранения изображений и связанной с ними информации
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(verbose_name='Ссылка на изображение')
    # verbose_name='URL' verbose_name='Картинка',
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    description = models.TextField(verbose_name='Описание',
                                   max_length=450,
                                   blank=True)
    # verbose_name='Дата и время создания',
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True,
                                   default=timezone.now)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)
    user_dislike = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                          related_name='images_disliked',
                                          blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
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
        происходит сохранение объекта изображения.
        """

        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.created.year,
                                              self.created.month,
                                              self.created.day,
                                              self.slug])
