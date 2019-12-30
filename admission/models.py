from django.db import models
import datetime
# Create your models here.
class Admission(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField(null=True,blank=True)
    enrolled_program = models.CharField(max_length=100)
    gender = models.CharField(choices=(('male','Male'),('female','Female')),max_length=10)
    special_needs = models.BooleanField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)
    counsellor = models.CharField(null=True,blank=True,max_length=100)

    def __init__(self):
        return self.fullname


    class Meta:
        db_table ='admission'


class Slc(models.Model):
    insitute_name = models.CharField(max_length=100)
    year_passed = models.DateField(null=True,blank=True)
    percentage = models.FloatField(null=True,blank=True)
    student  = models.OneToOneField(Admission,on_delete=models.CASCADE)


    def __init__(self):
        return self.student.name

    class Meta:
        db_table = 'slc'


class PlusTwo(models.Model):
    insitute_name = models.CharField(max_length=100)
    year_passed = models.DateField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    student = models.OneToOneField(Admission, on_delete=models.CASCADE)


    def __init__(self):
        return self.student.name

    class Meta:
        db_table ='plustwo'


class Master(models.Model):
    insitute_name = models.CharField(max_length=100)
    year_passed = models.DateField(null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    student = models.OneToOneField(Admission, on_delete=models.CASCADE)


    def __init__(self):
        return self.student.name

    class Meta:
        db_table ='master'


class Fee(models.Model):
    fee = models.IntegerField(null=True,blank=True)
    student = models.OneToOneField(Admission,on_delete=models.CASCADE)

    class Meta:
        db_table = 'fee'

    def __str__(self):
        return self.student

class Payment(models.Model):
    date = models.DateField(default=datetime.date.today)
    amount_paid = models.IntegerField()
    account = models.ForeignKey(Fee,on_delete=models.CASCADE)
    receivedby = models.CharField(max_length=100)


    def __str__(self):
        return self.amount_paid

    class Meta:
        db_table = 'payment'





