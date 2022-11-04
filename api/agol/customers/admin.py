from django.contrib import admin
from customers.models import Customer, Order

# Register your models here.
@admin.register(Customer)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','name', 'email']

# Register your models here.
@admin.register(Order)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id', 'customer','destination', 'order_quantity', 'order_status', 'driver', 'truck', 'trailer']
