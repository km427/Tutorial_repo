from rest_framework import serializers
from testapp.models import Student,teacher,User,subjects

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['username']

class teacherserializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = [
            'user',
            'teacher_name',
            'sub'
        ]
        depth = 1


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'student_name',
            'te',
        ]
        depth = 2



class updatesubjecSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = ('teacher_name', 'sub')