# Generated by Django 5.1.3 on 2024-12-01 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twix', '0010_profile_facebook_link_profile_homepage_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='homepage_link',
            new_name='email_link',
        ),
    ]