# Generated by Django 5.1.4 on 2024-12-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_title', models.CharField(max_length=100, verbose_name='Название новости')),
                ('n_desc', models.CharField(max_length=200, verbose_name='Краткое описание новости')),
                ('n_text', models.TextField(verbose_name='Новость')),
                ('n_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('n_author', models.CharField(max_length=100, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]