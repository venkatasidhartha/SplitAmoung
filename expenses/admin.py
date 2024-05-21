from django.contrib import admin
from expenses import models
# Register your models here.

class CustomPanelExpenseGroup(admin.ModelAdmin):
    list_display = ["id","name","created_at"]
    list_display_links = ["name"]
    list_filter = ["id","name"]
    search_fields = ["name"]

class CustomPanelExpense(admin.ModelAdmin):
    list_display = ["id","expense_grp_id","payer_id","amount"]
    list_display_links = ["expense_grp_id"]
    list_filter = ["id","expense_grp_id","payer_id"]
    search_fields = ["expense_grp_id","payer_id"]



admin.site.register(models.ExpenseGroup,CustomPanelExpenseGroup)
admin.site.register(models.Expense,CustomPanelExpense)
admin.site.register(models.ExpenseShare)


