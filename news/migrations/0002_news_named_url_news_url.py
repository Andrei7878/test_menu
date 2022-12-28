# Generated by Django 4.1.4 on 2022-12-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='named_url',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название ссылки'),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка'),
        ),
    ]