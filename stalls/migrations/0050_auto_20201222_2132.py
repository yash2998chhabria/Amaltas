# Generated by Django 2.2.14 on 2020-12-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0049_auto_20201222_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='stall_frame',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stall_frame',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
