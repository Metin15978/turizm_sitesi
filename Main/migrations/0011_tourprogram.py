# Generated by Django 4.2.10 on 2024-08-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_item_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_program_title', models.CharField(max_length=100, verbose_name='Tour Program Title')),
                ('tour_program_mini_title', models.CharField(max_length=100, verbose_name='Tour Program Mini Title')),
                ('tour_day_first', models.CharField(help_text='Gün Aralığı Giriniz örn:(Gün 1-2)', max_length=255, verbose_name='Tour Day First')),
                ('tour_day_first_title', models.CharField(max_length=100, verbose_name='Tour Day First Title')),
                ('tour_day_first_detail', models.TextField(max_length=255, verbose_name='Tour Day First Detail')),
            ],
        ),
    ]
