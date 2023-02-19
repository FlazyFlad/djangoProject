# Generated by Django 4.1.6 on 2023-02-19 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.category'),
        ),
    ]