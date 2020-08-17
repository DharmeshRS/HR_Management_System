"""HRMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Manager import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.homepageManager,name='managerhomepage'),
    path('validateManager/',views.validateManager,name="validateManager"),
    #recruitment
    path('recruitments/',views.recruitmentDetails,name="recruitments"),
    #interview schedule
    path('interviewschedule/',views.interviewschedule,name="interviewschedule"),
    #recruitment
    path('new_recruitment/',views.newrecruitment,name="new_recruitment"),
    path('saverecruitmentdetails/',views.saverecruitmentdetails,name="saverecruitmentdetails"),
    path('modifyrecruitmentdetails/',views.modifyrecruitmentdetails,name="modifyrecruitmentdetails"),
    path('savemodifyrecruitmentdetails/',views.savemodifyrecruitmentdetails,name="savemodifyrecruitmentdetails"),
    path('saverecruitment/',views.saveupdaterecruitment,name="saveupdaterecruitment"),
    path('deleterecruitment/',views.deleterecruitment,name="deleterecruitment"),
    path('deleterecruitmentconfirm/',views.deleterecruitmentconfirm,name="deleterecruitmentconfirm"),
    #interview schedule
    path('saveinterviewschedule/',views.saveinterviewschedule,name="saveinterviewschedule"),
    path('saveinterviewscheduledetails/',views.saveinterviewscheduledetails,name="saveint_detailsdata"),
    #back
    path('back/',views.backtomanager,name="backtomanager")



]
