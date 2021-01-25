from rest_framework import serializers
from .models import Deal, HistoryDeals


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['deal', 'customer', 'item', 'total', 'quantity', 'date']

