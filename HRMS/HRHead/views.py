from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from Applicant.models import ApplicationformModel, RegistrationModel
from H_Admin.models import EmployeeModel
from Interviewer.models import InterviewSchedule


def homepage(request):
    return render(request, "common/login/hrhead.html")


def validatehr(request):
    hr_username = request.POST["hr_username"]
    hr_password = request.POST["hr_password"]
    designation = "HRHead"
    print(hr_username,hr_password,designation)
    try:
        if EmployeeModel.objects.get(EmployeeName=hr_username, Password=hr_password,
                                     Designation=designation):
            messages.success(request, "Login Successfully")
            return render(request, "HRHead/hrheadoperations.html",
                          {"applicantdata": ApplicationformModel.objects.all()})
    except EmployeeModel.DoesNotExist:
        messages.success(request, "Invalid Credentials")
        return redirect('hrheadhomepage')


def shortlistedApplicants(request):
    return render(request, "HRHead/shortlistedApplicant.html", {"allapplicants": ApplicationformModel.objects.all()})


def selectedApplicants(request):
    status = "selected"
    try:
        it = InterviewSchedule.objects.get(status=status)
        ad=it.ApplicantID
        print(ad)
        return render(request, "HRHead/selectedapplicants.html",{"it":it} )
    except InterviewSchedule.DoesNotExist:
        return render(request, "HRHead/selectedapplicants.html")



def rejectedApplicants(request):
    status = "rejected"
    try:
        it = InterviewSchedule.objects.filter(status=status)
        return render(request, "HRHead/selectedapplicants.html", {"it": it})
    except InterviewSchedule.DoesNotExist:
        return render(request, "HRHead/selectedapplicants.html")

