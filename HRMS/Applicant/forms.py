from django import forms
from django.forms import ValidationError
from Applicant.models import RegistrationModel,ApplicationformModel
class RegistrationForm(forms.ModelForm):
    YEARS=[x for x in range(1980,2020)]
    DOB=forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender=(("male","male"),("female","female"))
    Gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect)
    def clean_Mobile_No(self):
        cno=self.cleaned_data['Mobile_No']
        scno=str(cno)
        l=len(scno)
        if l==10:
            return cno
        else:
            raise ValidationError("Invalid Contact No")
    class Meta:
        model=RegistrationModel
        fields="__all__"

class ApplicationformForm(forms.ModelForm):
    YEARS = [x for x in range(1985, 2020)]
    DOB = forms.DateField(widget=forms.SelectDateWidget(years=YEARS),label="Date Of Birth")
    gender = (("male", "male"), ("female", "female"))
    Gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect)
    Resume_upload_to=forms.FileField()

    def clean_Mobile_No(self):
        cno = self.cleaned_data['Mobile_No']
        scno = str(cno)
        l = len(scno)
        if l == 10:
            return cno
        else:
            raise ValidationError("Invalid Contact No")

    class Meta:
        model = ApplicationformModel
        fields = "__all__"