from django.db import models
from django.db.models.fields import DateField
from django.forms import fields
from django.forms.forms import Form
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('empID', 'empName', 'directory', 'Manager')


 
class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
        fields =[ 'empID', 'empName', 'directory'


        ] 


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('orgName', )


class RecordsForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ('RecordOwner', 'empDocs', 'empImages', )
