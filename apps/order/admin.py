import datetime

from django.urls import reverse
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


def order_name(obj):
    return  '%s %s' % (obj.first_name, obj.last_name)


order_name.short_description = 'Name'


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))


order_name.short_description = 'PDF Title'


def admin_order_shipped(modeladmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()

        html = render_to_string('order_sent.html', {'order': order})
        send_mail('Order sent', 'Your order is seccessful!', 'noreplay@saulgadgets.com', ['mail@saulgadgtes.com', order.email], fail_silently=False, html_message=html)
    
    return


admin_order_shipped.short_description = 'Set shipped'


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'status', 'created', order_pdf]
    list_filter = ['created', 'status']
    search_fields = ['first_name', 'address']
    inlines = [OrderItemInLine]
    actions = [admin_order_shipped]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
