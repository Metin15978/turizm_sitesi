# Generated by Django 4.2.10 on 2024-08-05 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0029_rename_author_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPromosions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Main.item')),
            ],
        ),
    ]
