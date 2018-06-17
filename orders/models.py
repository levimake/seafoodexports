from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.FloatField(blank=False, null=False)
    
    TYPE_CHOICES = (
            ('fish', 'Fish'),
            ('meat', 'Meat')
        )

    STATUS_CHOICES = (
            ('pending', 'PENDING'),
            ('processed', 'PROCESSED'),
            ('completed', 'COMPLETED')
        )

    type = models.CharField(max_length=40, choices=TYPE_CHOICES)
    delivery_address = models.TextField()
    company_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
