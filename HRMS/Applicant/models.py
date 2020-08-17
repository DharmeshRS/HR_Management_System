from django.db import models
from Manager.models import RecruitmentModel
from H_Admin.models import EmployeeModel

# Create your models here.
class RegistrationModel(models.Model):
    RegistrationID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    DOB=models.DateField()
    Email=models.EmailField(unique=True)
    Gender=models.CharField(max_length=30)
    Mobile_No=models.IntegerField(unique=True)
    Address=models.CharField(max_length=100)
    Username=models.CharField(unique=True,max_length=30)
    Password=models.CharField(max_length=30)

class ApplicationformModel(models.Model):
    ApplicantID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    DOB=models.DateField()
    Email_ID=models.EmailField(unique=True)
    Gender=models.CharField(max_length=30)
    Mobile_No=models.IntegerField(unique=True)
    Address=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=30)
    Post=models.ForeignKey(RecruitmentModel,on_delete=models.CASCADE)
    Percentage=models.DecimalField(max_digits=6,decimal_places=3)
    Resume_upload_to=models.FileField(upload_to='resume/')
    status=models.CharField(max_length=10,default=True)


