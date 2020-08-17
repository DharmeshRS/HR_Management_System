from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    EmployeeID=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=40)
    Password=models.CharField(max_length=300)
    Designation=models.CharField(max_length=40)
    Address=models.CharField(max_length=100)
    Contact_No=models.IntegerField(unique=True)
    EmailID=models.EmailField(unique=   True)