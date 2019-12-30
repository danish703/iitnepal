from django.db import models

# Create your models here.
class Training(models.Model):
    programme = models.CharField(max_length=100)

    class Meta:
        db_table  ='training'
