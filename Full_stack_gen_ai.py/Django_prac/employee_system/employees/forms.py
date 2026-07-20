from django import forms
from .models import Employee
from .models import Attendance

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = "__all__"