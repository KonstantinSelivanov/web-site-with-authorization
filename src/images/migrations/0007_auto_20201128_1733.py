# Generated by Django 2.2 on 2020-11-28 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20201127_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Загрузите изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]