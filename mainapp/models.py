from django.db import models
from django.db.models import Avg, Min, Max, Sum


class Shop(models.Model):
    name = models.CharField(max_length=127)
    time_start = models.TimeField()
    time_end = models.TimeField()
    address = models.CharField(max_length=127)

    def __str__(self):
        return self.name

    @property
    def sum_ticket_price(self):
        return self.tickets.aggregate(Sum('price'))['price__sum']

    def avg_ticket_price(self):
        return self.tickets.aggregate(Avg('price'))['price__avg']

    def max_ticket_price(self):
        return self.tickets.aggregate(Max('price'))['price__max']

    def min_ticket_price(self):
        return self.tickets.aggregate(Min('price'))['price__min']


class Ticket(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=127)
    price = models.PositiveIntegerField(default=0)
    replace_from = models.CharField(max_length=127)
    replace_to = models.CharField(max_length=127)

    def __str__(self):
        return self.name
