# Generated by Django 4.1.3 on 2022-11-04 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.CharField(max_length=10000),
        ),
    ]
