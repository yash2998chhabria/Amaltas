# Generated by Django 2.2.14 on 2020-07-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0029_auto_20200723_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall_frame',
            name='cover',
            field=models.ImageField(default='', upload_to='newcoverimages'),
        ),
        migrations.AlterField(
            model_name='stall_products',
            name='product_image',
            field=models.ImageField(default='', upload_to='products_images'),
        ),
    ]
