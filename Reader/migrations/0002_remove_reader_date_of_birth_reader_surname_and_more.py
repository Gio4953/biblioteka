# Generated by Django 4.2.1 on 2023-06-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='reader',
            name='surname',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='reader',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
