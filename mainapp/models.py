from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.contrib.auth.models import User

# Create your models here.
""" 
   create a model for employees 
   employees should id should be unique
   employee payement id is refferenced to pay role app
   """

class Organisation(models.Model):
    orgName = models.CharField(max_length=100, verbose_name="Organisation")

    def __str__(self) -> str:
        return self.orgName


class Directory(models.Model):
    parent_org = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")

    
class Employee(models.Model):
    empID = models.IntegerField(unique=True, verbose_name="Staff ID")
    empName = models.CharField(max_length=100, verbose_name="Staff Name")
    Updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    Entrydate = models.DateField(auto_created=True, auto_now_add=True)
    directory = models.ForeignKey(
          Directory, on_delete=models.CASCADE, default=True, null=True)
    Manager = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.empName

    objects = models.Manager()

class Payroll(models.Model):
    payementId = models.IntegerField(unique=True)
    staffinfor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    paydate = models.DateTimeField()
    amount = models.IntegerField()
    status = models.BooleanField(verbose_name="PAYEMENT STATUS", default=False)

    def __str__(self) -> str:
        return str(self.amount) and str(self.staffinfor)


class Records(models.Model):
    RecordOwner = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='+')
    empDocs = models.FileField(
        upload_to='media/documents', max_length=500, verbose_name='Documents')
    empImages = models.ImageField(upload_to='media/images', max_length=500,
                                  height_field=None, width_field=None, verbose_name="Images")
    Entrydate = models.DateField(auto_created=True, auto_now_add=True)

    def __str__(self) -> str:
        return str(self.RecordOwner)


class Tags(models.Model):
    record = models.ForeignKey(
        Records, related_name='tags', on_delete=models.CASCADE, related_query_name='tags')
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
