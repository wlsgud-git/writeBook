# Generated by Django 3.2.7 on 2022-03-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_users_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/default-user.jpg', null=True, upload_to='images/'),
        ),
    ]