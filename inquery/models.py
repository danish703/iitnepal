from django.db import models
import datetime
# Create your models here.
class Inquery(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=100,null=True,blank=True)
    course = models.CharField(max_length=100)
    counselor = models.CharField(max_length=100,null=True,blank=True)
    remarks = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table ='inquery'