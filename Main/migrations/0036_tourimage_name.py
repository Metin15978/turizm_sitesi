# Generated by Django 4.2.8 on 2024-08-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0035_tour_detail_remove_tour_tour_day_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourimage',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Ad'),
            preserve_default=False,
        ),
    ]