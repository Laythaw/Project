from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    enrollment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )


    class Meta:
        model = Student
        fields = ['first_name', 'middle_initial', 'last_name', 'email', 'date_of_birth', 'course', 'enrollment_date']
