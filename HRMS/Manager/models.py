from django.db import models
from H_Admin.models import EmployeeModel
# Create your models here.

class RecruitmentModel(models.Model):
    OpportunityCode=models.IntegerField(primary_key=True)
    Qualification=models.CharField(max_length=30)
    Registration_start_date=models.DateField()
    Age_limit=models.IntegerField()
    Last_date_of_apply=models.DateField()
    Department_id=models.CharField(max_length=30)
    No_Of_Positions=models.IntegerField()
    Description=models.CharField(max_length=400)
    Responsibilities=models.CharField(max_length=100)
    Contact_no=models.IntegerField()




