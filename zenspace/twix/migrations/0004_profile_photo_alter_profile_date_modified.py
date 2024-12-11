# Generated by Django 5.1.3 on 2024-11-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0003_profile_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
