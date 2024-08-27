from django.contrib import admin
from .models import  VehicleType, Activity, Museum, Hotel, Tour, TourImage, Item, ItemImage,TeamsModel, Comment,HotelImage,VehicleTypeImage,activityImage,Tour_detail
#  ItemPromosions
# Register your models here.
class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInline]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)


class VehicleTypeImageInline(admin.TabularInline):
    model = VehicleTypeImage
    extra = 1

class VehicleTypeAdmin(admin.ModelAdmin):
    inlines = [VehicleTypeImageInline]

admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(VehicleTypeImage)
# -----------------------------------------------
class activityImageInline(admin.TabularInline):
    model = activityImage
    extra = 1  # Varsayılan olarak bir tane boş form gösterir

class ActivityAdmin(admin.ModelAdmin):
    inlines = [activityImageInline]
    
admin.site.register(Activity, ActivityAdmin)
admin.site.register(activityImage)
admin.site.register(Museum)
admin.site.register(TourImage)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(TeamsModel)
admin.site.register(Comment)
admin.site.register(Tour)
admin.site.register(Tour_detail)





