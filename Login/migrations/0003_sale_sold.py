# Generated by Django 4.2.10 on 2024-08-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_remove_customer_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
