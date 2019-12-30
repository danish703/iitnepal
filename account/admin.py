from django.contrib import admin
from .models import Income,Expenses
# Register your models here.
admin.site.register([Income,Expenses])
