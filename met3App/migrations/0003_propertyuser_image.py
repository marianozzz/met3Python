# Generated by Django 2.2 on 2020-10-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('met3App', '0002_auto_20201023_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyuser',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
