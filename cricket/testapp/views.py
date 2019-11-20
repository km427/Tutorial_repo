from django.views.generic import CreateView
from testapp.models import teacher
from testapp.forms import StudentSignUpForm,login_form
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from testapp.serializers import studentserializer
from rest_framework import viewsets
from testapp.serializers import updatesubjecSerializer
from rest_framework.response import Response
from testapp.models import Student,User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,UpdateAPIView
from django.http import JsonResponse
from django.views.generic import ListView

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'testapp/signup.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = False
        return context
    def form_valid(self, form):
        user = form.save()
        return redirect('/login')



class Student_details_api(ListAPIView):
    def get(self,request,*args,**kwargs):
        # getting user object in users table
        user=User.objects.get(username=request.user)
        student_dict = {}
        print("studentttttttttttttttttt",request.user,user.is_student)
        if user.is_student:
            student_obj=Student.objects.get(user=user)
            student_dict["student_name"]=student_obj.student_name
            student_dict['id']=student_obj.user_id
            student_dict['username']=user.username
            qs=student_obj.te.all()
            teacher_final=[]
            for x in qs.values_list():
                t_dict={}
                t_dict['id']=x[0]
                t_dict['name']=x[1]
                t_u = User.objects.get(id=x[0])
                # creating teacher object
                teacher_obj=teacher.objects.get(user=t_u)
                subjects=teacher_obj.sub.all()
                sub_list=[]
                for x in subjects.values_list():
                    sub_list.append(x[1])
                t_dict['subjects']=sub_list
                teacher_final.append(t_dict)
            student_dict['teachers']=teacher_final
        else:
            student_dict={'Validation error':'User is Not A Student'}
        return JsonResponse(student_dict)
    serializer_class = studentserializer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes =[IsAuthenticated,]


class reportview(ListView):
    model = Student
    template_name = 'testapp/report.html'

    def get(self,request,*args,**kwargs):
        obj=Student.objects.all()
        details = []
        # getting student details
        for st in obj:
            empty_dict={}
            user_obj = User.objects.get(id=st.user_id)
            empty_dict['id']=st.user_id
            stud_obj=Student.objects.get(user=user_obj)
            empty_dict['student name'] = stud_obj.student_name
            qs = st.te.all()
            t=[]
            s=[]
            # getting teacher details
            for x in qs.values_list():
                t.append(x[1])
                t_u = User.objects.get(id=x[0])
                teacher_obj = teacher.objects.get(user=t_u)
                subjects = teacher_obj.sub.all()
                # getting subjects of partcular teacherrr
                for x in subjects.values_list():
                    s.append(x[1])
            t1=','.join(t)
            empty_dict['teachers'] = t1
            s1=','.join((s))
            empty_dict['Subjects'] = s1
            details.append(empty_dict)
        return render(request,'testapp/report.html',{'details':details})

class Updatestudentsubject(viewsets.ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = updatesubjecSerializer
    # def partial_update(self, request, pk=None):
    #     serializer = updatesubjecSerializer(request.user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


def login(request):
    print('userd')
    form=login_form()
    if request.method=='POST':
        form=login_form(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if hasattr(user, 'is_student'):
               # You'll return to student app
                return redirect('/report')
    return  render(request,'registration/login.html',{'form':form})


