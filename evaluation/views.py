from django.shortcuts import render,get_object_or_404


from rest_framework.views import APIView

from rest_framework import permissions,authentication

from rest_framework.response import Response

from rest_framework import serializers

from rest_framework.generics import UpdateAPIView


from exam.models import Assessment

from exam.serializers import AssessmentSerializer


from problem.models import Question


from evaluation.permissions import IsStudentUser

from evaluation.models import Submission,Answer

from evaluation.serializers import SubmissionSerializer,AnswerSerializer


from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class SubmissionStartView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def post(self,request,pk=None):

        # here nothing in form_data . thats y no isvalid function

        assessment_id = pk

        assessment_object = get_object_or_404(Assessment,id=assessment_id)

        instance =Submission.objects.create(assessment=assessment_object,student=request.user)

        serializer_instance = SubmissionSerializer(instance)

        return Response(data=serializer_instance.data)

class AnswerCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudentUser]

    def post(self,request,pk=None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id=submission_id)

        form_data = request.data

        #validation starts

        assessment_object = submission_object.assessment

        assessment_questions = Question.objects.filter(assessment=assessment_object).values_list("id",flat=True)
                                                                                     # to convert dictionary into list           

        question_id = form_data.get("question")

        if question_id not in assessment_questions:

            raise serializers.ValidationError("invalid question , question not exist in this assessment")

        #validation ends

        serializer_instance = AnswerSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(submission=submission_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        instance = get_object_or_404(Submission,id=pk)

        serializer_instance = SubmissionSerializer(instance)

        return  Response(data=serializer_instance.data)

class AnswerUpdateView(UpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = AnswerSerializer

    queryset = Answer.objects.all()

    def patch(self,request,pk=None):

        answer_id = pk

        answer_object = get_object_or_404(Answer,id=answer_id)

        form_data = request.data

        #validation starts

        question_object = answer_object.question

        score = question_object.score

        if form_data.get("marks_awarded") > score:

            raise serializers.ValidationError("invalid mark")


        #validation ends 

        serializer_instance = AnswerSerializer(data=form_data,instance=answer_object,partial=True)

        serializer_instance.fields["marks_awarded"].read_only = False

        serializer_instance.fields["feedback"].read_only = True

        if serializer_instance.is_valid():

            print(serializer_instance.validated_data)

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

        

        