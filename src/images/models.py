from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.template.defaultfilters import slugify as slugify_ru
from django.urls import reverse
from django.utils import timezone


alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
            'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
            'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
            'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
            'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding slugify_ru that allows to use russian words as well.
    Переопределение slugify_ru, позволяющее также использовать русские слова.
    """
    return slugify_ru(''.join(alphabet.get(w, w) for w in s.lower()))


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
    image = models.ImageField(verbose_name='Загрузите изображение',
                              upload_to='image/%Y/%m/%d')
    description = models.TextField(verbose_name='Описание',
                                   max_length=450,
                                   blank=True)
    created = models.DateTimeField(verbose_name='Дата и время создания',
                                   db_index=True, default=timezone.now)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    users_dislike = models.ManyToManyField(settings.AUTH_USER_MODEL,
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
        return reverse('images:detail', args=[self.id, self.slug])
