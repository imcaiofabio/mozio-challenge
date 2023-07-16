from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name