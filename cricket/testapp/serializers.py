from rest_framework import serializers
from testapp.models import Student,teacher,User,subjects

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields ="__all__"


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class updatesubjecSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = ('teacher_name', 'sub')