# Generated by Django 3.0.4 on 2020-04-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200409_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(default='', upload_to='property_manage'),
        ),
    ]