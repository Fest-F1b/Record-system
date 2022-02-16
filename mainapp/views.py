
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import generic
from mainapp.forms import *
from django.contrib import messages
from . models import *
from django.db.models import Q
from django.db.models import Count
from django.forms import *
from django.core.paginator import Paginator
from users.models import Profile
import datetime as dt

import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# create views for


def orgstructure(request):
    template_name = 'mainapp/index.html'
    org = Organisation.objects.all()
    return render(request, template_name, {'org': org})


class PostList(generic.ListView):
    queryset = Organisation.objects.all()
    template_name = 'mainapp/index.html'

# EMPLOYEE ENTRY DASHBOARD
# Dashboard is to display all employees in the database
# Paginate employees when a list of 12 employees is listed.
# Paginator will create a page for every list of 10 employees


def dashboard(request):
    person = Employee.objects.all()
    paginator = Paginator(person, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mainapp/dashboard.html', {'page_obj': page_obj})

# EMPLOYEE RECORDS DETAILS
# Function to get employee files from the database


def empprofile(request, pk):
    empdetails = Records.objects.get(pk=pk)
    return render(request, 'mainapp/empprofile.html', ({'empdetails': empdetails}))


#  ADD EMPLOYEES
# Add Employee form
# Function cleaneses and saves employees added
def addemployee(request):
    template_name = 'mainapp/addemp.html'

    if request.method == 'POST':
        EnterEmployee_form = EmployeeForm(data=request.POST)
        if EnterEmployee_form.is_valid():
            entry = EnterEmployee_form.save(commit=False)
            entry.save()
            messages.success(request, f'Employee successfuly added')
            return HttpResponseRedirect('mainapp/dashboard.html')
    else:
        EnterEmployee_form = EmployeeForm()

    if request.method == 'POST':
        Org_form = OrganisationForm(data=request.POST)
        if Org_form.is_valid():
            org_entry = Org_form.save(commit=False)
            org_entry.save()
    else:
        Org_form = OrganisationForm()

    if request.method == 'POST':
        recordform = RecordsForm(data=request.POST)
        if recordform.is_valid():
            record_entry = recordform.save(commit=False)
            record_entry.save()
    else:
        recordform = RecordsForm()

    return render(request, template_name, {'EnterEmployee_form': EnterEmployee_form,
                                           'Org_form': Org_form, 'recordform': recordform})


# SEARCH VIEW
# The function gets both text and num queries
# queries and fetches results from database and are
# rendered in the template
def search(request):
    template = 'mainapp/search.html'

    query = request.GET.get('q')

    result = Employee.objects.filter(
        Q(empName__icontains=query) | Q(empID__icontains=query))
    context = {'employees': result}
    return render(request, template, context)


def testing(request):
    organize = Organisation.objects.all()
    return render(request, 'mainapp/index.html', ({'organize': organize}))


def dept_test(request):
    dept = Employee.objects.all()
    return render(request, 'mainapp/testing.html', ({'dept': dept}))


# PROFILE VIEW
# view for user profile page
def profp(request):
    userp = Profile.objects.all()
    return render(request, 'emprecord\profile.html', ({'userp': userp}))

# CSV FUNCTION TO POST AND CLEAN DATA TO MODEL
def Import_csv(request):
    print('s')
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file, f'file uploaded')
            empexceldata = pd.read_csv("."+excel_file, encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                fromdate_time_obj = dt.datetime.strptime(
                    dbframe.DOB, '%d-%m-%Y')
                obj = Employee.objects.create(empID=dbframe.empID, empName=dbframe.empName,
                                              directory=dbframe.directory)
                print(type(obj))
                obj.save()

            return render(request, 'mainapp/importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as identifier:
        print(identifier)

    return render(request, 'mainapp/importexcel.html', {})

# ERROR HANDLING FUNCTIONS
def page_not_found_view(request,exception):
    return render(request, '404.html',status=404)

def server_error_view(request,exception):
    return render (request, '500.html',status=500)

def http_forbidden_view(request,exception):
    return render(request, '403.html',status=403)

def bad_request_view(request,exception):
    return render(request, '400.html',status=400)