# Generated by Django 4.2.10 on 2024-08-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_item_tour_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='tour_program',
        ),
        migrations.DeleteModel(
            name='TourProgram',
        ),
    ]
