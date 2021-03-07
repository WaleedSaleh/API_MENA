from django.db import models

# Create your models here.

class BTC (models.Model):
    crypto_currency = models.CharField(max_length=10, verbose_name="Crypto Currency", null=False, blank=False, default="BTC")
    price = models.FloatField(verbose_name="Price", null=False, blank=False)
    exchange_rate = models.FloatField(verbose_name="Exchange Rate", null= False, blank=True)
    currency = models.CharField(max_length=10, verbose_name="Currency", null=False, blank=False, default="USD")
    created_at = models.DateTimeField(verbose_name = "Created At", auto_now=True)
    updated_at = models.DateTimeField(verbose_name="Updated At")

    class Meta:
        verbose_name = "BTC"
        verbose_name_plural = "BTCs"
        db_table = "btcs"

    def __repr__(self):
        return  self.price