from rest_framework import serializers

from accounts.models import User

from accounts.models import StudentProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudentProfile

        fields = "__all__"

        read_only_fields = ["id","student"]