# Generated by Django 2.2.14 on 2020-08-26 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0038_auto_20200826_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stall_products',
            name='category',
        ),
        migrations.AddField(
            model_name='stall_frame',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stalls.product_category'),
        ),
    ]
