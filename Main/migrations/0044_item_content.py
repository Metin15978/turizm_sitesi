# Generated by Django 4.2.8 on 2024-08-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0043_tour_detail_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='content',
            field=models.CharField(default=1, max_length=255, verbose_name='açıklama'),
            preserve_default=False,
        ),
    ]
