from rest_framework import serializers

from students.model.models import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('name', 'age')
