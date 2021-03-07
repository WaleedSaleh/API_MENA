from rest_framework import serializers
from .models import BTC

class BTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ['crypto_currency', 'price', 'exchange_rate','currency', 'updated_at']
        # field = "__all__"