# Generated by Django 2.2 on 2020-11-24 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201124_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileuser',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
    ]
