

Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Student, MarkStudent
from .serializers import StudentSerializer, MarkStudentSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

class MarkCreateAPIView(generics.CreateAPIView):
    queryset = MarkStudent.objects.all()
    serializer_class = MarkStudentSerializer

class MarkDetailAPIView(generics.ListAPIView):
    serializer_class = MarkStudentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return MarkStudent.objects.filter(student_id=pk)

class ResultsAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        students_with_marks = Student.objects.filter(markstudent__isnull=False)
        pass_percentage = (students_with_marks.count() - students_with_marks.filter(markstudent_mark_lt=50).count()) / students_with_marks.count() * 100

        grade_conditions = [
            (students_with_marks.filter(markstudent_mark_range=(91, 100)), 'S'),
            (students_with_marks.filter(markstudent_mark_range=(81, 90)), 'A'),
            (students_with_marks.filter(markstudent_mark_range=(71, 80)), 'B'),
            (students_with_marks.filter(markstudent_mark_range=(61, 70)), 'C'),
            (students_with_marks.filter(markstudent_mark_range=(51, 60)), 'D'),
            (students_with_marks.filter(markstudent_mark_range=(50, 55)), 'E'),
            (students_with_marks.filter(markstudent_mark_lt=50), 'F'),
        ]

        results = []
        for condition, grade in grade_conditions:
            result = {
                'grade': grade,
                'students': StudentSerializer(condition, many=True).data
            }
            results.append(result)

        results.append({'pass_percentage': pass_percentage})

        return results