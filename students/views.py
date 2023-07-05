from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from students.entity.students import Students
from rest_framework import status


class StudentsAPIView(APIView):

    def get(self, request):
        stlist = Students.objects.all().values()
        return Response({'students': list(stlist)})

    def post(self, request):
        name = request.data.get('name')
        age = request.data.get('age')
        profile_image = request.data.get('profile_image')

        new_student = Students.objects.create(
            name=name,
            age=int(age),
            profile_image=profile_image if profile_image else None
        )

        return Response({'post': model_to_dict(new_student)})

    def patch(self, request, student_id):
        name = request.data.get('name')
        age = request.data.get('age')
        profile_image = request.data.get('profile_image')

        try:
            student = Students.objects.get(id=student_id)
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        if name:
            student.name = name
        if age:
            student.age = age
        if profile_image:
            student.profile_image = profile_image

        student.save()

        return Response({'patch': model_to_dict(student)})

    def put(self, request, student_id):
        name = request.data.get('name')
        age = request.data.get('age')
        profile_image = request.data.get('profile_image')

        try:
            student = Students.objects.get(id=student_id)
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student.name = name
        student.age = age
        student.profile_image = profile_image

        student.save()

        return Response({'patch': model_to_dict(student)})

    def delete(self, request, student_id):

        try:
            student = Students.objects.get(id = student_id)
        except Students.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        student.delete()

        return Response({'patch': model_to_dict(student)})
