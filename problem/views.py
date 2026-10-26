from django.shortcuts import render


from rest_framework.views import APIView

from rest_framework import authentication,permissions

from rest_framework.response import Response

from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView


from exam.models import Assessment


from problem.serializers import QuestionSerializer

from problem.models import Question

# Create your views here.
class QuestionCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_object = Assessment.objects.get(id=assessment_id)

        form_data = request.data

        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(assessment=assessment_object,created_by = request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()