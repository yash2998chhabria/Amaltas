# Generated by Django 2.2.14 on 2020-12-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0050_auto_20201222_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall_products',
            name='position',
            field=models.IntegerField(default=100),
        ),
    ]
