# Generated by Django 3.2.2 on 2021-05-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_merge_20210509_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(default='/profile_images/avatar.png', upload_to='profile_images'),
        ),
    ]
