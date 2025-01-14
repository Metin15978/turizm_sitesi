# Generated by Django 4.2.10 on 2024-08-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_alter_tour_tour_day_title'),
        ('Login', '0009_remove_sale_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='Main.item', verbose_name='Item')),
            ],
        ),
    ]
