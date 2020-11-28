# Generated by Django 2.2 on 2020-11-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20201127_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique_for_date='created'),
        ),
    ]
