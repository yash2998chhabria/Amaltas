# Generated by Django 2.2.14 on 2020-08-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0033_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
