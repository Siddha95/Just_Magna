from django.contrib import admin
from .models import *

admin.site.register(Voucher)
admin.site.register(Cart)
admin.site.register(Cart_dish)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Invoice)

