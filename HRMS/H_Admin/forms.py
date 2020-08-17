from django import forms
from H_Admin.models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    EmployeeName=forms.CharField(max_length=30)
    Password=forms.CharField(max_length=30,widget=forms.PasswordInput)
    desig=(("Admin","Admin"),
           ("Interviewer","Interviewer"),("HRHead","HRHead"),
           ("Manager","Manager"),("Applicant","Applicant"))
    Designation=forms.ChoiceField(choices=desig)
    Address=forms.CharField()



    class Meta:
        model=EmployeeModel
        fields="__all__"
        exclude=('EmployeeID',)