from django.contrib import admin
from .models import Employee
# Register your models here.

# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_active", "date_joined"]
    list_editable = ["is_active"]
    list_filter = ["is_active", "date_joined"]
