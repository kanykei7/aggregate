from rest_framework import serializers
from mainapp.models import (Shop, Ticket)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'shop', 'name', 'price', 'replace_from', 'replace_to',
        )


class ShopSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(read_only=True, many=True)

    class Meta:
        model = Shop
        fields = (
            'name', 'time_start', 'time_end', 'address', 'tickets',
            'sum_ticket_price','avg_ticket_price', 'max_ticket_price', 'min_ticket_price',
        )
