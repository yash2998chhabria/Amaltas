# Generated by Django 2.2 on 2020-06-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200602_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='emaildata',
            name='whatsapp',
            field=models.BigIntegerField(null=True),
        ),
    ]
