# Generated by Django 3.2.2 on 2021-05-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='isFound',
        ),
        migrations.AddField(
            model_name='barang',
            name='status',
            field=models.CharField(choices=[('FOUND', 'FOUND'), ('LOST', 'LOST')], max_length=10, null=True),
        ),
    ]