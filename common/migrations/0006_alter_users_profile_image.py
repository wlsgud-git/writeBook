# Generated by Django 3.2.7 on 2022-03-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_users_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
