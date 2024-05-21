from django.db import models
from django.conf import settings
# Create your models here.


class ExpenseGroup(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,blank=False,null=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='expense_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Expense(models.Model):
    expense_grp = models.ForeignKey(ExpenseGroup,on_delete=models.DO_NOTHING,blank=False,null=False)
    payer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,blank=False,null=False)
    amount = models.FloatField(blank=False,null=False)
    s3_file_id = models.PositiveIntegerField(blank=False,null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ExpenseShare(models.Model):
    expense = models.ForeignKey(Expense,on_delete=models.DO_NOTHING,blank=False,null=False)
    member = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,blank=False,null=False)
    share_amount = models.FloatField(blank=False,null=False)