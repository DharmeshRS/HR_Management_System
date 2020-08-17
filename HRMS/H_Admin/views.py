from django.shortcuts import render, redirect
from django.contrib import messages
from H_Admin.forms import EmployeeForm,EmployeeModel
# Create your views here.
def homepageAdmin(request):
    return render(request, "common/login/loginformadmin.html")


def validateAdmin(request):
    admin_username=request.POST["username"]
    admin_password=request.POST["password"]
    try:
        if admin_username=="admin" and admin_password=="admin":
            messages.success(request, "Successfully Login ")
            return render(request,"H_Admin/Admin_homepage.html")
        else:
            messages.success(request, "Invalid Credentials")
            return render(request, "common/login/loginformadmin.html")
    except KeyError:
        messages.success(request, "Invalid Credentials")
        return render(request, "common/login/loginformadmin.html")


def addEmployee(request):
    ef = EmployeeForm
    return render(request,"H_Admin/AddEmployee.html",{"employeeform":ef})


def saveemployee(request):
    ef = EmployeeForm(request.POST)
    if ef.is_valid():
        ef.save()
        return redirect('AddEmployee')
    else:
        return render(request, "H_Admin/AddEmployee.html", {"employeeform": ef})


def viewemployee(request):
    return render(request,"H_Admin/ViewEmployee.html",{"data":EmployeeModel.objects.all()})


def deleteEmployee(request):
    checkbox=request.POST.getlist("checkbox")
    if checkbox==[]:
        messages.error(request,"You Can't Select Any Record")
    print("ck",checkbox)
    for x in checkbox:
        print(x)
    # eid=request.GET.get("eid")
    # enm=request.GET.get("enm")
        EmployeeModel.objects.filter(EmployeeID=x).delete()
        messages.success(request,"Data Deleted Successfully")
    return render(request,"H_Admin/DeleteEmployee.html",{"data":EmployeeModel.objects.all()})

def updateEmployee(request):
    # eid=request.GET.get("eid")
    # employeeform=EmployeeModel.objects.get(EmployeeID=eid)
    # print(employeeform)
    return render(request,"H_Admin/UpdateEmployee.html",{"data":EmployeeModel.objects.all()})


def updateEmployeeform(request):
    eid=request.GET.get("eid")
    employeeform=EmployeeModel.objects.get(EmployeeID=eid)
    print(employeeform)
    return render(request,"H_Admin/UpdateEmployeeform.html",{"data":employeeform})


def saveupdateEmployeeform(request):
    eid=request.POST["employeeid"]
    enm=request.POST["employeename"]
    password=request.POST["Password"]
    designation=request.POST["designation"]
    address=request.POST["address"]
    cno=request.POST["contactno"]
    email=request.POST["emailid"]
    EmployeeModel(EmployeeID=eid,EmployeeName=enm,Password=password,Designation=designation,Address=address,Contact_No=cno,EmailID=email).save()
    # EmployeeModel.objects.filter(EmployeeID=eid).update(EmployeeName=enm,Password=password,Designation=designation,Address=address)
    return redirect('updateEmployee')