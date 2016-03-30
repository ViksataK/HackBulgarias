from django.db import models


class User(models.Model):
    username = models.CharField(max_length=140, primary_key=True)
    password = models.CharField(max_length=140)

    @classmethod
    def login(cls, username, password):
        try:
            u = cls.objects.get(username=username, password=password)
            return u
        except cls.DoesNotExist:
            return None
# Create your models here.
