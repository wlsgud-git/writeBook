# Generated by Django 3.2.7 on 2022-03-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_books_create_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
