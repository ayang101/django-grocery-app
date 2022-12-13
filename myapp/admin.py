from django.contrib import admin
from .models import Group, Item, ReceiptItem, Receipt

admin.site.register(Group)
admin.site.register(Item)
admin.site.register(ReceiptItem)
admin.site.register(Receipt)
