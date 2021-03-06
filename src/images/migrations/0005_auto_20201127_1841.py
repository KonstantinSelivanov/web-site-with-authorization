# Generated by Django 2.2 on 2020-11-27 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20201127_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(verbose_name='Ссылка на изображение'),
        ),
    ]
