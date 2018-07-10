from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'


    @classmethod
    def create(cls, username, email,
               password):
        
        try:
            object = cls(username=username,
                         email=email,
                         password=make_password(password),
                        )

            object.save()
            return object

        except Exception as e:
            print(e)

    @classmethod
    def submit(cls, id, first_name, last_name,
               country, password, phone_number,
               address):

        user = cls.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.country = country
        user.password = make_password(password)
        user.phone_number = phone_number
        user.address = address
        
        user.completed = True

        user.save()

        return user
    

    @classmethod
    def update(cls, id, password, address, phone_number):

        user = cls.objects.get(id = id)
        user.password = password
        user.address = address
        user.phone_number = phone_number

        user.save()

        return user

    
    @classmethod
    def login(cls, username, password):
        object = cls.objects.get(username = username)
        return check_password(password, object.password)


    @classmethod
    def update_password(cls, id, password):
        user = cls.objects.get(id=id)
        user.password = password
        user.save()


    @classmethod
    def update_address(cls, id, address):
        user = cls.objects.get(id=id)
        user.address = address
        user.save()


    @classmethod
    def update_phone(cls, id, phone_number):
        user = cls.objects.get(id=id)
        user.phone_number = phone_number
        user.save()
