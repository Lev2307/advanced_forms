from django.contrib import admin
from .models import OrderModel, OrderProxy

# Register your models here.
class OrderInline(admin.TabularInline):
    model = OrderProxy
    verbose_name = 'order'
    verbose_name_plural = 'Create order'
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]
    exclude = ('pizza_order',)
    list_display = ('address', 'time', 'all_orders')
admin.site.register(OrderModel, OrderAdmin)