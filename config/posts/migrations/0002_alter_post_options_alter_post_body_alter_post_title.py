# Generated by Django 4.1.7 on 2023-03-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-uploaded_at'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='Содержание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Заголовок', max_length=50),
        ),
    ]
