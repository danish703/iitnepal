from django.db import models
import datetime

class Income(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(default=datetime.date.today)
    remarks = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table ='Income'


class Expenses(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(default=datetime.date.today)
    remarks = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table ='Expenses'