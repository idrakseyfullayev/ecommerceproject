# Generated by Django 4.1.7 on 2023-04-05 14:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_rename_product_productmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ViewNumber',
            new_name='ViewNumberModel',
        ),
    ]
