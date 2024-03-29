# Generated by Django 4.1.6 on 2023-03-31 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_category_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(blank=True, default=None, null=True, unique=True),
        ),
    ]
