# Generated by Django 4.2.1 on 2023-06-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0002_remove_reader_date_of_birth_reader_surname_and_more'),
        ('Book', '0002_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(related_name='books', to='Reader.reader'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
    ]
