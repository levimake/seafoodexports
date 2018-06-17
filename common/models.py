from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'


    @classmethod
    def create(cls, username, first_name, last_name, country,
               email, phone_number, password, address):
        
        object = cls(username=username,
                     first_name=first_name,
                     last_name=last_name,
                     country=country,
                     email=email,
                     phone_number=phone_number,
                     password=make_password(password),
                     address=address)

        object.save()
        return object


    @classmethod
    def login(cls, username, password):
        object = cls.objects.get(username = username)
        return check_password(password, object.password)
            
