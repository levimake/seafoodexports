from django.db import models
from django.utils import timezone

from common.models import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
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
    timestamp = models.DateTimeField(default=timezone.now)

    
    @classmethod
    def processed(cls, id):
        order = cls.objects.get(id=id)
        order.status = 'processed'
        order.save()


    @classmethod
    def completed(cls, id):
        order = cls.objects.get(id=id)
        order.status = 'completed'
        order.save()

    
    @classmethod
    def cancel(cls, id):
        order = cls.objects.get(id=id)
        cur_time = timezone.now()
        time_diff = cur_time - order.timestamp
        if time_diff > 259200:
            return False
        else:
            order.delete()
                
