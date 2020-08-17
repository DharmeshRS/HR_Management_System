from django import forms
from .models import RecruitmentModel
from Interviewer.models import  InterviewSchedule

class RecruitmentForm(forms.ModelForm):
    OpportunityCode = forms.IntegerField()
    Qualification = forms.CharField()
    Registration_start_date = forms.DateField(widget=forms.SelectDateWidget)
    Age_limit = forms.IntegerField(min_value=21,max_value=45)
    Last_date_of_apply =forms.DateField(widget=forms.SelectDateWidget)
    Department_id = forms.CharField(label="Department ID")
    No_Of_Positions = forms.IntegerField()
    Description = forms.CharField(widget=forms.Textarea)
    Responsibilities = forms.CharField()
    Contact_no = forms.IntegerField()

    class Meta:
        model=RecruitmentModel
        fields="__all__"


class InterviewScheduleForm(forms.ModelForm):
    class Meta:
        model=InterviewSchedule
        fields="__all__"