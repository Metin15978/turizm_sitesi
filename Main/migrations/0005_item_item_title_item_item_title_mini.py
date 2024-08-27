# Generated by Django 4.2.10 on 2024-08-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_item_end_date_item_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_title',
            field=models.CharField(default='', max_length=255, verbose_name='Item Title'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_title_mini',
            field=models.CharField(default='', max_length=255, verbose_name='Item Mini Title'),
        ),
    ]