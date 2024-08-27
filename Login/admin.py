from django.contrib import admin
from.models import Customer, Sale
from django.utils.html import format_html
# Register your models here.

admin.site.register(Sale)

class CustomerAdmin(admin.ModelAdmin):
    # Liste görünümünde gösterilecek alanlar
    list_display = ('user_username', 'get_first_name', 'get_last_name','email', 'tckn', 'passport_number', 'slug')

    # Detay sayfasında gösterilecek alanlar
    fieldsets = (
        (None, {
            'fields': ('user', 'tckn', 'passport_number', 'slug')
        }),
        ('User Information', {
            'fields': ('get_first_name', 'get_last_name', 'user_username', 'email')
        }),
    )
    readonly_fields = ('slug', 'get_first_name', 'get_last_name', 'user_username', 'email')  # Kullanıcı bilgileri sadece okunabilir

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Username'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')

admin.site.register(Customer, CustomerAdmin)