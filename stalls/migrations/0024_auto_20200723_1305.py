# Generated by Django 2.2.14 on 2020-07-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0023_auto_20200723_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall_frame',
            name='cover',
            field=models.ImageField(upload_to='coverimages'),
        ),
    ]
