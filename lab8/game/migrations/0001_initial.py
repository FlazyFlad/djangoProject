# Generated by Django 4.1.6 on 2023-02-28 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('desciption', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category_id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Тема новости')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.author')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.category')),
            ],
            options={
                'verbose_name': 'Наши новости',
                'verbose_name_plural': 'Наши новости',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True)),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.news')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.user')),
            ],
        ),
    ]
