from django.contrib import messages
from django.shortcuts import render, redirect
from Manager.forms import RecruitmentModel,RecruitmentForm,InterviewSchedule
from Applicant.models import ApplicationformModel
from H_Admin.models import EmployeeModel


# Create your views here.
def homepageManager(request):
    return render(request, "common/login/managerlogin.html")


def validateManager(request):
    manager_username=request.POST["manager_username"]
    manager_password=request.POST["manager_password"]
    if manager_username=="manager" and manager_password=="manager":
        messages.success(request,"Login Successful")
        return render(request,"Manager/manager_homepage.html")
    else:
        messages.error(request,"Invalid Credentials")
        return redirect('managerhomepage')


def recruitmentDetails(request):
    return render(request,"Manager/manager_recruitment.html")


def interviewschedule(request):
    #for inout applicant ID
    applicantform=ApplicationformModel.objects.all()
    return render(request,"Manager/manager_interviewschedule.html",{"applicantform":applicantform})


def newrecruitment(request):
    rs=RecruitmentForm()
    return render(request,"Manager/newrecruitmentdetails.html",{"recruitmentform":rs})


def saverecruitmentdetails(request):
    rs=RecruitmentForm(request.POST)
    if rs.is_valid():
        rs.save()
        messages.success(request,"Data Is Saved")
        return redirect('new_recruitment')
    else:
        # messages.error(request,"Invalid Data Format")
        # return redirect('new_recruitment')
        return render(request,"Manager/newrecruitmentdetails.html",{"recruitmentform":rs})


def modifyrecruitmentdetails(request):
    return render(request,"Manager/modifyrecruitmentdetails.html")

def savemodifyrecruitmentdetails(request):
    opcode=request.POST.get("opcode")
    try:
        rs=RecruitmentModel.objects.get(OpportunityCode=opcode)
        return render(request, "Manager/updaterecruitmentpage.html",
                      {"recruitmentform": RecruitmentForm, "recruitmentdata": rs})
    except RecruitmentModel.DoesNotExist:
        messages.error(request,"Invalid OpportunityCode")
        return redirect('modifyrecruitmentdetails')

    # return redirect('new_recruitment')



def saveupdaterecruitment(request):
    opcode=request.POST["opcode"]
    qualification=request.POST["qualification"]
    sdate=request.POST["sdate"]
    age=request.POST["agelimit"]
    ldate=request.POST["ldate"]
    departid=request.POST["deptid"]
    positions=request.POST["positions"]
    description=request.POST["description"]
    responsibility=request.POST["respon"]
    cno=request.POST["cno"]
    RecruitmentModel(OpportunityCode=opcode,Qualification=qualification,Registration_start_date=sdate,
                     Age_limit=age,Last_date_of_apply=ldate,Department_id=departid,No_Of_Positions=positions,
                     Description=description,Responsibilities=responsibility,Contact_no=cno).save()
    messages.success(request,"Data Is Modified")
    return redirect('recruitments')


def deleterecruitment(request):
    return render(request, "Manager/deleterecruitmentdetails.html", {"recruitmentdata":RecruitmentModel.objects.all()})


def deleterecruitmentconfirm(request):
    opcode=request.POST.getlist("opcode")
    print(type(opcode))
    for x in opcode:
        RecruitmentModel.objects.filter(OpportunityCode=x).delete()
        messages.success(request,"Data Is Deleted")
    return redirect('deleterecruitment')


#interview schedule data

def saveinterviewschedule(request):
    applicantid=request.POST["applicantid"]
    print(applicantid)
    return render(request, "Manager/AssignInterviewpage.html", {"interviewform":EmployeeModel.objects.all(),
                                                      "applicantid":applicantid})


def saveinterviewscheduledetails(request):
    applicantid=request.POST["applicantid"]
    empid=request.POST["empid"]
    sdate=request.POST["scheduledate"]
    status="pending"
    print(applicantid,empid,sdate,status)
    InterviewSchedule(ApplicantID=applicantid,Emp_id_id=empid,schedule_date=sdate,status=status).save()
    messages.success(request, "Schedule Is Set")
    return redirect('interviewschedule')


def backtomanager(request):
    return render(request,"Manager/manager_homepage.html")