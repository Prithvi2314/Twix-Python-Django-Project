# Generated by Django 5.1.3 on 2024-11-23 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0005_profile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
    ]
