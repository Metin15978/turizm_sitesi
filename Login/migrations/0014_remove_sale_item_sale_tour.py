# Generated by Django 4.2.10 on 2024-08-09 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0050_alter_tour_item'),
        ('Login', '0013_alter_sale_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='item',
        ),
        migrations.AddField(
            model_name='sale',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.tour', verbose_name='Tour'),
        ),
    ]
