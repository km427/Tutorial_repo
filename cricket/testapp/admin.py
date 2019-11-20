from django.contrib import admin
from testapp.models import Student,User,teacher,subjects
from testapp.forms import teachersform,studentform
class studentadmin(admin.ModelAdmin):
    form = studentform
    list_display = ['user','student_name','Teachers']

    def Teachers(self, obj):
        return "\n".join([str(p.user) for p in obj.te.all()])
admin.site.register(Student,studentadmin)


class useradmin(admin.ModelAdmin):
    list_display = ['id','username','email','is_student','is_teacher']
admin.site.register(User,useradmin)


class techeradmin(admin.ModelAdmin):
    form = teachersform
    list_display = ['user','teacher_name','subjects']
    def subjects(self, obj):
        return "\n".join([p.name for p in obj.sub.all()])
admin.site.register(teacher,techeradmin)

class subjectsadmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(subjects,subjectsadmin)