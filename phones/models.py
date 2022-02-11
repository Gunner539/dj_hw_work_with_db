from django.db import models
from datetime import datetime


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.CharField(max_length=300)
    release_date = models.DateField(default=datetime.now())
    lte_exists = models.BooleanField(default=False)
    slug = models.CharField(max_length=150)
    # pass
