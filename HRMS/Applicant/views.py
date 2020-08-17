from django.contrib import messages
from django.shortcuts import render, redirect
from Manager.models import RecruitmentModel
from Applicant.forms import RegistrationForm,RegistrationModel,ApplicationformModel,ApplicationformForm
# Create your views here.
def homepageApplicant(request):
    return render(request, "common/login/applicantlogin.html")


def validateApplicant(request):
    Applicant_username = request.POST["Applicant_username"]
    Applicant_password = request.POST["Applicant_password"]
    print(Applicant_username,Applicant_password)
    try:
        if RegistrationModel.objects.filter(Username=Applicant_username,Password=Applicant_password):
            messages.success(request, "Login Successfully")
            return render(request, "Applicant/newapplicationform.html",{"applicantform":RecruitmentModel.objects.all()})
            # return render(request, "Applicant/newapplicationform.html",{"applicantform":ApplicationformForm()})
    except RegistrationModel.DoesNotExist:
        messages.success(request, "Invalid Credentials")
    return redirect('applicant')


            # return render(request,"Applicant/homepageApplicant.html",{})


def newregistration(request):
    return render(request,"Applicant/newregistration.html")


def saveregistration(request):
    name=request.POST['full_name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    contact=request.POST['phone']
    address=request.POST['address']
    try:
        RegistrationModel(Name=name,DOB=dob,Gender=gender,Username=username,Password=password,
                          Email=email,Mobile_No=contact,Address=address).save()
        messages.success(request,"Registration Successful")
        return redirect('applicant')
    except RegistrationModel.DoesNotExist:
        messages.error(request, "Invalid Format")
        return render(request,"Applicant/newregistration.html",{"applicantform":af})


def newappicationform(request):
    applicantform=RecruitmentModel.objects.all()
    # RecruitmentModel.objects.all()
    # applicantform= ApplicationformForm()
    return render(request, "Applicant/newapplicationform.html", {"applicantform":applicantform})


def saveapplicantform(request):
    name=request.POST["name"]
    dob=request.POST["dob"]
    email=request.POST["email"]
    gender=request.POST["radio"]
    mobileno=request.POST["mobileno"]
    address=request.POST["address"]
    qualification=request.POST["qualification"]
    post=request.POST["post"]
    percentage=float(request.POST["percentage"])
    uploadresume=request.FILES["upload"]
    status="Shortlisted"
    print(name,dob,email,gender,mobileno,address,qualification,percentage,uploadresume)
    ApplicationformModel(Name=name,DOB=dob,Email_ID=email,Gender=gender,Mobile_No=mobileno,Address=address,
                         Qualification=qualification,Post_id=post,Percentage=percentage,Resume_upload_to=uploadresume,status=status).save()

    messages.success(request, "Application Submitted Successfully")
    return redirect('applicantform')
    # else:
    #     messages.error(request, "Invalid Format")
    #     return render(request, "Applicant/newapplicationform.html", {"applicantform": applicantform})
