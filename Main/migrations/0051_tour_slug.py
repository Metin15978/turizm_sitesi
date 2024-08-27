# Generated by Django 4.2.8 on 2024-08-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0050_alter_tour_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=255, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
