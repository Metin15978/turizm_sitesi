# Generated by Django 4.2.10 on 2024-08-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_remove_item_tour_program_delete_tourprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tour_day_first',
            field=models.CharField(default='', max_length=255, verbose_name='Tour Day First'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_first_detail',
            field=models.TextField(default='', max_length=255, verbose_name='Tour Day First Detail'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_first_title',
            field=models.CharField(default='', max_length=100, verbose_name='Tour Day First Title'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_fourth',
            field=models.CharField(default='', max_length=255, verbose_name='Tour Day Fourth'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_fourth_detail',
            field=models.TextField(default='', max_length=255, verbose_name='Tour Day Fourth Detail'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_fourth_title',
            field=models.CharField(default='', max_length=100, verbose_name='Tour Day Fourth Title'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_second',
            field=models.CharField(default='', max_length=255, verbose_name='Tour Day Second'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_second_detail',
            field=models.TextField(default='', max_length=255, verbose_name='Tour Day Second Detail'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_second_title',
            field=models.CharField(default='', max_length=100, verbose_name='Tour Day Second Title'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_third',
            field=models.CharField(default='', max_length=255, verbose_name='Tour Day Third'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_third_detail',
            field=models.TextField(default='', max_length=255, verbose_name='Tour Day Third Detail'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_day_third_title',
            field=models.CharField(default='', max_length=100, verbose_name='Tour Day Third Title'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_program_mini_title',
            field=models.CharField(default='', max_length=100, verbose_name='Tour Program Mini Title'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_program_title',
            field=models.CharField(default='', max_length=100, verbose_name='Tour Program Title'),
        ),
    ]