# Generated by Django 4.2.10 on 2024-08-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_remove_comment_name_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]