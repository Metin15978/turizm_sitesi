# Generated by Django 4.2.10 on 2024-08-05 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0028_alter_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
    ]