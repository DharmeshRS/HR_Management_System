from django.contrib import messages
from django.shortcuts import render,redirect
from H_Admin.models import EmployeeModel
from Interviewer.models import InterviewSchedule

from Applicant.models import ApplicationformModel, RegistrationModel


# Create your views here.
def homepageInterviewer(request):
    return render(request, "common/login/interviewerlogin.html")


def validateInterviewer(request):
        Interviewer_username = request.POST["Interviewer_username"]
        Interviewer_password = request.POST["Interviewer_password"]
        designation="Interviewer"
        print(Interviewer_username,Interviewer_password,designation)
        try:
            if EmployeeModel.objects.get(EmployeeName=Interviewer_username,Password=Interviewer_password,Designation=designation):
                messages.success(request, "Login Successfully")
                return render(request, "Interviewer/selectionpage.html",
                              {"applicantdata": ApplicationformModel.objects.all()})
        except RegistrationModel.DoesNotExist:
            messages.success(request, "Invalid Credentials")
            return redirect('getdetail_ofapplicant')





def getdetail_ofapplicant(request):
    try:
        applicantid=request.POST["empid"]
        print(applicantid)

        interviewdetails=InterviewSchedule.objects.get(ApplicantID=applicantid)
        # print(interviewdetails.ApplicantID,interviewdetails.Emp_id_id,interviewdetails.schedule_dateinterviewdetails.status)
        return render(request, "Applicant/getdetailsofapplicant.html", {"interviewdetails":interviewdetails})
    except InterviewSchedule.DoesNotExist:
        messages.error(request, "Sorry No Any Interview Details")
        return render(request, "Interviewer/selectionpage.html", {"applicantdata": ApplicationformModel.objects.all()})


def applicant_statusresult(request):
    applicantid=request.POST["applicantid"]
    status=request.POST["status"]
    InterviewSchedule.objects.filter(ApplicantID=applicantid).update(status=status)
    messages.success(request, "Status been Updated Successfully")
    return render(request, "Interviewer/selectionpage.html", {"applicantdata": ApplicationformModel.objects.all()})