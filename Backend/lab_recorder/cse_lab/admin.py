from django.contrib import admin
from .models import Department, Lab, PurchaseOrder, Equipment

admin.site.register(Department)
admin.site.register(Lab)
admin.site.register(PurchaseOrder)
admin.site.register(Equipment)