# Generated by Django 3.0.6 on 2020-05-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0003_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='fullSizeUrl',
            field=models.URLField(blank=True, default=''),
        ),
    ]
