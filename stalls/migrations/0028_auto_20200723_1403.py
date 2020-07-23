# Generated by Django 2.2.14 on 2020-07-23 08:33

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0027_auto_20200723_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall_frame',
            name='cover',
            field=image_optimizer.fields.OptimizedImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stall_products',
            name='product_image',
            field=image_optimizer.fields.OptimizedImageField(upload_to=''),
        ),
    ]
