# Generated by Django 2.2.14 on 2020-08-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0037_auto_20200826_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='article',
            name='blogimg',
            field=models.ImageField(default='', upload_to='blogimgs'),
        ),
    ]
