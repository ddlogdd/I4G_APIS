# Generated by Django 4.0.5 on 2022-07-02 22:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Link',
        ),
    ]
