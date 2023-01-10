from django.db import models
from django.utils import timezone
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=None)
    category = models.CharField(max_length=100, blank=False)
    # item can be in many receipts
    receipts = models.ManyToManyField('Receipt', through='ReceiptItem')

    def price_per_unit(self):
        return round(self.price / self.quantity, 2)

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + " " + str(self.quantity)


class Receipt(models.Model):
    store = models.CharField(max_length=100)
    total_price = models.FloatField(max_length=5)
    date_visited = models.DateTimeField()
    # a receipt can have many items
    items = models.ManyToManyField('Item', through='ReceiptItem')

    def __str__(self):
        return self.store # + " " + self.date_visited


# through model (Item <-> Receipt)
class ReceiptItem(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, null=True, on_delete=models.CASCADE)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    groups = models.ManyToManyField('Group', through='Membership')
    # image = models.ImageField(upload_to='files/user_images')

    def __str__(self):
        return self.first_name + " " + self.last_name


# A group can have a couple of members where each member can be a part of
#   more than one group. Each group can have multiple receipts, and every
#   receipt is unique.
class Group(models.Model):
    name = models.CharField(max_length=100)
    # date_created = models.DateTimeField(default=timezone.now)
    # created_by
    members = models.ManyToManyField('Person', through='Membership')
    # image = models.ImageField(upload_to='files/group_images')
    receipts = models.ForeignKey(Receipt, null=True, on_delete=models.CASCADE)


# through model (Person <-> Group)
class Membership(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

"""
class Store(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
"""
