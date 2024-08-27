# Generated by Django 4.2.10 on 2024-08-03 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_alter_item_item_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Main.tour'),
            preserve_default=False,
        ),
    ]