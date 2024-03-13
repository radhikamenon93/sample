from django import forms
from work.models import Bookm,Student

class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()

class BookForm(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    year=forms.IntegerField()
    genre=forms.CharField()

class BookmForm(forms.ModelForm):
    class Meta:
        model=Bookm
        fields='__all__'
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'       

    