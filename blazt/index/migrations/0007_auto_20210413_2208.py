# Generated by Django 3.2 on 2021-04-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_songs_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='lang',
        ),
        migrations.AddField(
            model_name='songs',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]
