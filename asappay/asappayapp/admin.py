from django.contrib import admin
from .models import Account
from .models import Transaction

# Register your models here.

class accountAdmin(admin.ModelAdmin):
    list_display=[
        "accountid",
        "accountname",
        "accountemailid",
        "accountphone",
        "accountpan",
        "accountgst"
    ]
admin.site.register(Account,accountAdmin)

class transactionAdmin(admin.ModelAdmin):
    list_display=[
        "transactionid",
        "transactionname",
        "transactionemailid",
        "transactionphone",
        "transactionamount",
        "transactioncreatedate",
        "transactionduedate"
    ]
admin.site.register(Transaction,transactionAdmin)
