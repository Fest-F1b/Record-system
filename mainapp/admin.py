from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tags)

class EmployeeAdmin(admin.ModelAdmin):
   list_display = ('empID', 'empName','Updated',)

admin.site.register(Employee, EmployeeAdmin)

class PayrollAdmin(admin.ModelAdmin):
   list_display = ('staffinfor', 'paydate',)
   list_filter = ('status','paydate')

admin.site.register(Payroll, PayrollAdmin)

class RecordAdmin(admin.ModelAdmin):
   list_display = ('RecordOwner','empDocs')
   list_filter = ('Entrydate',)
   search_fields = ('RecordOwner',)

admin.site.register(Records, RecordAdmin)

class OrganisationAdmin(admin.ModelAdmin):
   list_display = ("orgName", )

admin.site.register(Organisation,OrganisationAdmin)

class DirectoryAdmin(admin.ModelAdmin):
   list_display = ("name", )

admin.site.register(Directory,DirectoryAdmin)