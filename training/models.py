from django.db import models

# Create your models here.
class Training(models.Model):
    programme = models.CharField(max_length=100)

    def __str__(self):return self.programme

    class Meta:
        db_table  ='training'
