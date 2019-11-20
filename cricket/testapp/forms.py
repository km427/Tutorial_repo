from django import forms
from django.contrib.auth.forms import UserCreationForm
from testapp.models import User,Student,teacher,subjects


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','is_student','is_teacher']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if user.is_teacher and user.is_student:
                raise forms.ValidationError("Please select student or teacher only one")
            elif user.is_student:
                st_obj = Student.objects.create(user=user,email=user.email,student_name=user)
            elif user.is_teacher:
                st_obj = teacher.objects.create(user=user,teacher_name=user)
        return user

class teachersform(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_teacher=True))
    teacher_name = forms.CharField(max_length=256)
    sub = forms.ModelChoiceField(queryset=subjects.objects.all())
    class Meta():
        model = teacher
        fields = ['user', 'teacher_name', 'sub']

class studentform(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_student=True))
    class Meta:
        model=Student
        fields='__all__'


class login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
