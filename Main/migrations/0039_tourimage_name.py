# Generated by Django 4.2.8 on 2024-08-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0038_remove_item_tourimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourimage',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Ad'),
            preserve_default=False,
        ),
    ]
