from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include
from os import name
from django.urls import path
from .import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('empprofile/<int:pk>/', views.empprofile, name='empprofile'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('search/', views.search, name='search'),
    path('testing', views.testing, name='testing'),
    path('dept_test', views.dept_test, name='dept_test'),
    path('profp', views.profp, name='profp'),
    path('Import_csv/', views.Import_csv,name="Import_csv"),  


]

handler404 = "mainapp.views.page_not_found_view"
handler403 = "mainapp.views.http_forbidden_view"
handler400 = "mainapp.views.bad_request_view"