# Generated by Django 2.2 on 2020-06-09 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0011_stall_products_choose_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_category',
            old_name='category',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='stall_products',
            old_name='choose_category',
            new_name='category',
        ),
    ]
