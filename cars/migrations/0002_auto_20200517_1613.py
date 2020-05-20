# Generated by Django 2.0 on 2020-05-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='Make',
            field=models.CharField(max_length=100, verbose_name='Make'),
        ),
    ]
