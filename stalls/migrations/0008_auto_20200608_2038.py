# Generated by Django 2.2 on 2020-06-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0007_auto_20200608_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='stall_city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
