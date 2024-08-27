# Generated by Django 4.2.8 on 2024-08-08 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0045_tour_discount_price_alter_item_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='item',
        ),
        migrations.AddField(
            model_name='comment',
            name='Tour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Main.tour'),
            preserve_default=False,
        ),
    ]