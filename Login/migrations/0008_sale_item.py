# Generated by Django 4.2.10 on 2024-08-07 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_alter_tour_tour_day_title'),
        ('Login', '0007_remove_sale_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='Main.item', verbose_name='Item'),
        ),
    ]