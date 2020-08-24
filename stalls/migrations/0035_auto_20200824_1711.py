# Generated by Django 2.2.14 on 2020-08-24 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0034_auto_20200824_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
