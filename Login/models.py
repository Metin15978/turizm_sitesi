from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from Main.models import Item, Tour

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tckn = models.CharField(max_length=11, blank=True, null=True)
    passport_number = models.CharField(max_length=9, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.user.username

    def clean(self):
        # TCKN ve pasaport numarası doğrulama (örnek doğrulamalar)
        if self.tckn and len(self.tckn) != 11:
            raise ValidationError('TCKN 11 haneli olmalıdır.')
        if self.passport_number and len(self.passport_number) != 9:
            raise ValidationError('Pasaport numarası 9 haneli olmalıdır.')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Customer, self).save(*args, **kwargs)



class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales', verbose_name="Customer")
    tours = models.ManyToManyField(Tour)  # Burada ManyToManyField olmalı
    sold = models.BooleanField(default=False)
    
    is_delete = models.BooleanField(verbose_name="Deleted", default=False)
    delete_date = models.DateTimeField(verbose_name="Deletion Date", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Last Update Date", auto_now=True)

    def __str__(self):
        tour_names = ", ".join(tour.name for tour in self.tours.all())
        return f"{self.customer.user} - {tour_names}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)