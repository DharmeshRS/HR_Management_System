from django.db import models

from H_Admin.models import EmployeeModel


class InterviewSchedule(models.Model):
    ApplicantID=models.IntegerField()
    Emp_id=models.OneToOneField(EmployeeModel,on_delete=models.CASCADE)
    schedule_date=models.DateField()
    status=models.CharField(max_length=10)
