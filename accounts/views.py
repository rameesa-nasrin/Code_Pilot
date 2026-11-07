from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import authentication,permissions

from rest_framework_simplejwt.authentication import JWTAuthentication


from accounts.models import User,StudentProfile

from accounts.serializers import UserSerializer

from accounts.serializers import StudentProfileSerializer

from evaluation.permissions import IsStudentUser

# Create your views here.
class AdminCreateView(APIView):

    def post(Self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_superuser(role="admin",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class StudentCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(role="student",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class ProfileUpdateView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def put(self,request):

        form_data = request.data

        student_profile_object = StudentProfile.objects.get(student=request.user)

        #student_profile_object = request.user.student  # related_name=student

        serializer_instance = StudentProfileSerializer(data=form_data,instance=student_profile_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class ProfileDetailView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def get(self,request):

        instance = StudentProfile.objects.get(student=request.user)

        serializer_instance = StudentProfileSerializer(instance)

        return Response(data=serializer_instance.data)