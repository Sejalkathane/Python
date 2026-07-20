from django.shortcuts import render
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'employees/home.html')

def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'employees/employee_list.html',
        {'employees': employees}
    )

def employee_create(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, id):

    # Find employee by id
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":

        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employees/employee_form.html',
        {'form': form}
    )

def employee_delete(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":

        employee.delete()

        return redirect('employee_list')

    return render(
        request,
        'employees/employee_delete.html',
        {'employee': employee}
    )


def attendance_create(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('attendance_list')

    else:

        form = AttendanceForm()

    return render(
        request,
        'employees/attendance_form.html',
        {'form': form}
    )

def attendance_list(request):

    attendance = Attendance.objects.all()

    return render(
        request,
        'employees/attendance_list.html',
        {'attendance': attendance}
    )


def home(request):
    employees = Employee.objects.all()
    return render(request, "employees/home.html", {"employees": employees})





from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:

        form = AuthenticationForm()

    return render(
        request,
        'employees/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    return redirect('login')