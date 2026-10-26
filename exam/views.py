from django.shortcuts import render


from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication,permissions



from accounts.models import User


from exam.models import Assessment

from exam.serializers import AssessmentSerializer

from exam.permissions import IsOwner


from datetime import datetime,timedelta

# Create your views here.
class AssessmentListView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        instance = Assessment.objects.all()

        serializer_instance = AssessmentSerializer(instance,many=True)

        return Response(data=serializer_instance.data)

class AssessmentCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request):

        form_data = request.data

        serializer_instance = AssessmentSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(created_by=request.user)

            # cleaned_data = serializer_instance.validated_data

            # exam_date = cleaned_data.get("exam_date")

            # exam_start_time = cleaned_data.get("start_time")

            # duration = cleaned_data.get("duration")

            # end_date_time = datetime.combine(exam_date,exam_start_time)+timedelta(hours=duration)

            # end_time = end_date_time.time()

            # serializer_instance.save(end_time=end_time,created_by=request.user)

            #instance = Assessment.objects.create(**cleaned_data,end_time=end_time,created_by=request.user)

            #serializer_instance = AssessmentSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class AssessmentRetrieveUpdateView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = AssessmentSerializer

    queryset = Assessment.objects.all()


        
