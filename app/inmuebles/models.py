# This is an auto-generated Django model module.

from django.db import models


class Property(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=32)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'property'

    def __str__(self):
        return f'address:{self.address}'


class Status(models.Model):
    name = models.CharField(unique=True, max_length=32)
    label = models.CharField(max_length=64)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return f'status:{self.name}'


class StatusHistory(models.Model):
    property = models.ForeignKey(Property, models.DO_NOTHING)
    status = models.ForeignKey(Status, models.DO_NOTHING)
    update_date = models.DateTimeField()

    class Meta:
        db_table = 'status_history'

    def __str__(self):
        return f'date:{self.update_date}'
