# Generated by Django 4.2.10 on 2024-08-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0054_rename_tour_comment_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='content',
            field=models.TextField(verbose_name='Tur Programı Content'),
        ),
        migrations.AlterField(
            model_name='item',
            name='end_day',
            field=models.IntegerField(help_text='Gün sayısını girin', verbose_name='Program Bitiş Günü'),
        ),
        migrations.AlterField(
            model_name='item',
            name='start_day',
            field=models.IntegerField(help_text='Gün sayısını girin', verbose_name='Program Başlangıç Günü'),
        ),
        migrations.AlterField(
            model_name='tour_detail',
            name='tour_program_mini_title',
            field=models.CharField(max_length=100, verbose_name='Tour Detail Mini Title'),
        ),
        migrations.AlterField(
            model_name='tour_detail',
            name='tour_program_title',
            field=models.CharField(max_length=100, verbose_name='Tour Detail Title'),
        ),
    ]