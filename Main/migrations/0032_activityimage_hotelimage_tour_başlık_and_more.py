# Generated by Django 4.2.8 on 2024-08-08 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0031_alter_tour_tour_day_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='activityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='activity_images/', verbose_name='Image')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Deleted')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Deletion Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Update Date')),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hotel_images/', verbose_name='Image')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Deleted')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Deletion Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Update Date')),
            ],
        ),
        migrations.CreateModel(
            name='Tour_başlık',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('day', models.IntegerField(blank=True, null=True, verbose_name='Day')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Deleted')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Deletion Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Update Date')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_image', to='Main.tourimage')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTypeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vehicle_icons/', verbose_name='Icon')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Deleted')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='Deletion Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Last Update Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='itempromosions',
            name='item',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='item',
            name='TourImage',
        ),
        migrations.RemoveField(
            model_name='item',
            name='day',
        ),
        migrations.RemoveField(
            model_name='item',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_detail',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_title_mini',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='vehicletype',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='item',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='item',
            name='museum',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='DayImage',
        ),
        migrations.DeleteModel(
            name='ItemPromosions',
        ),
        migrations.AddField(
            model_name='vehicletypeimage',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Main.vehicletype'),
        ),
        migrations.AddField(
            model_name='tour_başlık',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Main.item'),
        ),
        migrations.AddField(
            model_name='hotelimage',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Main.hotel'),
        ),
        migrations.AddField(
            model_name='activityimage',
            name='Activity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Main.activity'),
        ),
        migrations.AddField(
            model_name='item',
            name='activity',
            field=models.ManyToManyField(related_name='items', to='Main.activity'),
        ),
        migrations.AddField(
            model_name='item',
            name='hotel',
            field=models.ManyToManyField(related_name='items', to='Main.hotel'),
        ),
        migrations.AddField(
            model_name='item',
            name='museum',
            field=models.ManyToManyField(related_name='items', to='Main.museum'),
        ),
    ]
