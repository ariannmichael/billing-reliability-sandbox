from django.db import models


class Payment(models.Model):
    ext_payment_id = models.CharField(max_length=64, unique=True)
    amount_cents = models.IntegerField()
    currency = models.CharField(max_length=8)
    status = models.CharField(max_length=16) # succeeded|failed
    updated_at = models.DateField(auto_now=True)


class WebhookEvent(models.Model):
    ext_event_id = models.CharField(max_length=64, unique=True)
    type = models.CharField(max_length=64) # payment_intent.succeeded
    payload = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)

class IdempotencyKey(models.Model):
    key = models.CharField(max_length=128, primary_key=True)
    status = models.CharField(max_length=16) # processed|in_progress|failed
    response_code = models.IntegerField(default=200)
    created_at = models.DateTimeField(auto_now_add=True)