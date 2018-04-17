from django.contrib import admin
from . import models



admin.site.register(models.UserProfile)
admin.site.register(models.MemberType)
admin.site.register(models.Credit)
admin.site.register(models.CreditRecharge)
admin.site.register(models.CreditTransfer)
admin.site.register(models.PaymentNote)

