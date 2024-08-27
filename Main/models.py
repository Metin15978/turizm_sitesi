from django.db import models
from django.utils.text import slugify
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class TeamsModel(models.Model):
    ROLE_CHOICES = [
        ('Sale Manager', 'Sale Manager'),
        ('Co-Founder & CFO', 'Co-Founder & CFO'),
        ('Technical Lead & CTO', 'Technical Lead & CTO'),
        ('Marketing Manager', 'Marketing Manager'),
    ]
    name = models.CharField(max_length=255, verbose_name="Name")
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='team_images/', verbose_name="Image")
    content = models.CharField(max_length=100, verbose_name="content")

    def __str__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class VehicleType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class VehicleTypeImage(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicle_icons/', verbose_name="Icon")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return f"Image for {self.vehicle_type.name}"


class Activity(models.Model):
    LOCATION_CHOICES = [
        ('adana', 'Adana'),
        ('adıyaman', 'Adıyaman'),
        ('afyonkarahisar', 'Afyonkarahisar'),
        ('ağrı', 'Ağrı'),
        ('amasya', 'Amasya'),
        ('ankara', 'Ankara'),
        ('antalya', 'Antalya'),
        ('artvin', 'Artvin'),
        ('aydin', 'Aydın'),
        ('balıkesir', 'Balıkesir'),
        ('bilecik', 'Bilecik'),
        ('bingöl', 'Bingöl'),
        ('bitlis', 'Bitlis'),
        ('bolu', 'Bolu'),
        ('burdur', 'Burdur'),
        ('bursa', 'Bursa'),
        ('çanakkale', 'Çanakkale'),
        ('çankırı', 'Çankırı'),
        ('çorum', 'Çorum'),
        ('denizli', 'Denizli'),
        ('diyarbakır', 'Diyarbakır'),
        ('düzce', 'Düzce'),
        ('edirne', 'Edirne'),
        ('elazığ', 'Elazığ'),
        ('erzincan', 'Erzincan'),
        ('erzurum', 'Erzurum'),
        ('eskişehir', 'Eskişehir'),
        ('gaziantep', 'Gaziantep'),
        ('giresun', 'Giresun'),
        ('gümüşhane', 'Gümüşhane'),
        ('hakkari', 'Hakkari'),
        ('hatay', 'Hatay'),
        ('ısparta', 'Isparta'),
        ('istanbul', 'İstanbul'),
        ('izmir', 'İzmir'),
        ('kahramanmaraş', 'Kahramanmaraş'),
        ('karabük', 'Karabük'),
        ('karaman', 'Karaman'),
        ('kars', 'Kars'),
        ('kastamonu', 'Kastamonu'),
        ('kayseri', 'Kayseri'),
        ('kırıkkale', 'Kırıkkale'),
        ('kırklareli', 'Kırklareli'),
        ('kırşehir', 'Kırşehir'),
        ('klise', 'Kilis'),
        ('kocaeli', 'Kocaeli'),
        ('konya', 'Konya'),
        ('kütahya', 'Kütahya'),
        ('malatya', 'Malatya'),
        ('manisa', 'Manisa'),
        ('mardin', 'Mardin'),
        ('mersin', 'Mersin'),
        ('muğla', 'Muğla'),
        ('muş', 'Muş'),
        ('nevşehir', 'Nevşehir'),
        ('nigde', 'Niğde'),
        ('ordu', 'Ordu'),
        ('osmaniye', 'Osmaniye'),
        ('rize', 'Rize'),
        ('sakarya', 'Sakarya'),
        ('samsun', 'Samsun'),
        ('siirt', 'Siirt'),
        ('sinop', 'Sinop'),
        ('sivas', 'Sivas'),
        ('şanlıurfa', 'Şanlıurfa'),
        ('şırnak', 'Şırnak'),
        ('tekirdağ', 'Tekirdağ'),
        ('tokat', 'Tokat'),
        ('trabzon', 'Trabzon'),
        ('tunceli', 'Tunceli'),
        ('uşak', 'Uşak'),
        ('van', 'Van'),
        ('yalova', 'Yalova'),
        ('yozgat', 'Yozgat'),
        ('zonguldak', 'Zonguldak')
    ]

    name = models.CharField(max_length=255, verbose_name="Name")
    location = models.CharField(
        max_length=255, 
        choices=LOCATION_CHOICES, 
        verbose_name="Location"
    )
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class activityImage(models.Model):
    Activity_type = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='activity_images/', verbose_name="Image")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return f"Image for {self.Activity_type.name}"

class Museum(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    image = models.ImageField(upload_to='museum_images/', verbose_name="Image")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class Hotel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel_images/', verbose_name="Image")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return f"Image for {self.hotel.name}"


class Tour_detail(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    tour_program_title = models.CharField(max_length=100, verbose_name='Tour Detail Title') # DEĞİŞKEN ADLARINA DİKKAT YAĞIZ
    tour_program_mini_title = models.CharField(max_length=100, verbose_name='Tour Detail Mini Title') # DEĞİŞKEN ADLARINA DİKKAT YAĞIZ
    details = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TourImage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ad")
    image = models.ImageField(upload_to='tour_images/')
    is_delete = models.BooleanField(default=False)
    delete_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{datetime.now().timestamp()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Image"
    
class ItemImage(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    image = models.ImageField(upload_to='item_images/', verbose_name="Image")
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   
        
class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ad")
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, related_name='items')
    activity = models.ManyToManyField(Activity, related_name='items')
    museum = models.ManyToManyField(Museum, related_name='items')
    hotel = models.ManyToManyField(Hotel, related_name='items')
    start_day = models.IntegerField(verbose_name="Program Başlangıç Günü", help_text="Gün sayısını girin")
    end_day = models.IntegerField(verbose_name="Program Bitiş Günü", help_text="Gün sayısını girin")
    location = models.CharField(max_length=255, verbose_name="şehir")
    content = models.TextField(verbose_name="Tur Programı Content") 
    item_image = models.ForeignKey(ItemImage, on_delete=models.CASCADE, related_name='images')
    is_delete = models.BooleanField(verbose_name="Silindi", default=False)
    delete_date = models.DateTimeField(verbose_name="Silinme Tarihi", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Son Güncellenme Tarihi", auto_now=True)

    def __str__(self):
        return self.name 

    def clean(self):
        if self.start_day > self.end_day:
            raise ValidationError("Başlangıç günü, bitiş gününden büyük olamaz.")




class Tour(models.Model):
    name = models.CharField(max_length=255, verbose_name="Adı")
    slug = models.SlugField(unique=True, editable=False, verbose_name="Slug")  # Add slug field
    item = models.ManyToManyField(Item, related_name='tours')
    Tour_detail = models.ForeignKey(Tour_detail, on_delete=models.CASCADE, related_name='Tour_detail')
    image = models.ForeignKey(TourImage, on_delete=models.CASCADE, related_name='tour_image')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="İndirimli Fiyat", blank=True, null=True)
    day = models.IntegerField(verbose_name="Gün", blank=True, null=True)
    is_delete = models.BooleanField(verbose_name="Silindi", default=False)
    delete_date = models.DateTimeField(verbose_name="Silinme Tarihi", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Son Güncelleme Tarihi", auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug if it doesn't exist
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




class Comment(models.Model):
    tour = models.ForeignKey(Tour, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    
    
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.tour.name}'
    
