# Generated by Django 2.2 on 2020-06-25 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0014_stall_frame_stall_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall_products',
            name='stall_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stalls.stall_frame'),
        ),
    ]
