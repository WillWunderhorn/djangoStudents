from rest_framework import serializers

from students.entity.students import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('name', 'age')
