# Generated by Django 3.2.7 on 2022-03-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_users_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(blank=True, default='media/images/user-image-icon-16.jpg', null=True, upload_to='images/'),
        ),
    ]