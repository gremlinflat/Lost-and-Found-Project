# Generated by Django 3.2.2 on 2021-05-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_prodi_nama_prodi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodi',
            name='nama_prodi',
            field=models.CharField(max_length=50),
        ),
    ]