# Generated by Django 3.0.5 on 2020-04-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgdesc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgdescdb',
            name='photo',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
