# Generated by Django 4.2.10 on 2024-08-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0030_itempromosions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_day_title',
            field=models.CharField(max_length=100, verbose_name='Tour Day Title'),
        ),
    ]