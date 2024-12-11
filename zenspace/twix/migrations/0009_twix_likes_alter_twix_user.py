# Generated by Django 5.1.3 on 2024-11-27 08:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0008_alter_profile_profile_image_alter_twix_photo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='twix',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='twix_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='twix',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]