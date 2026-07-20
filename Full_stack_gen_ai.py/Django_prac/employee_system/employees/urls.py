

from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
   path('home/', views.home, name='home'),
path('logout/', views.logout_view, name='logout'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_create'),

    path(
    'employees/update/<int:id>/',
    views.employee_update,
    name='employee_update'
),

path(
    'employees/delete/<int:id>/',
    views.employee_delete,
    name='employee_delete'
),

path(
    'attendance/add/',
    views.attendance_create,
    name='attendance_create'
),

path(
    'attendance/',
    views.attendance_list,
    name='attendance_list'
),

]