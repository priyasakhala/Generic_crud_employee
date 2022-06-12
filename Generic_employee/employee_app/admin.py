from django.contrib import admin
from .models import Employee

# Register your models here.

class EmloyeeAdmin(admin.ModelAdmin):

    list_display = ['eid','ename','branch','salary','city']
admin.site.register(Employee,EmloyeeAdmin)
