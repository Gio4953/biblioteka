# Generated by Django 4.2.1 on 2023-06-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
