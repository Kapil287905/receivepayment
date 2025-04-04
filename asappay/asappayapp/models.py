from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

# Create your models here.

class Account(models.Model):
    accountid = models.PositiveIntegerField(primary_key=True)
    userid = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=None)
    accountname = models.CharField(max_length=100)
    accountemailid = models.EmailField()
    accountphone = PhoneNumberField()
    accountpan = models.CharField(max_length=10)
    accountgst = models.CharField(max_length=15)

class Transaction(models.Model):
    transactionid = models.PositiveIntegerField(primary_key=True)
    userid = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=None)
    transactionname = models.CharField(max_length=100)
    transactionemailid = models.EmailField()
    transactionphone = PhoneNumberField()
    transactionamount = models.FloatField()
    transactioncreatedate = models.DateField()
    transactionduedate = models.DateField()
