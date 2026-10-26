from rest_framework import serializers

from exam.models import Assessment

from accounts.models import User

from datetime import datetime


class AssessmentSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    class Meta:

        model = Assessment

        fields = "__all__"

        read_only_fields = ["id","end_time","created_by"]

    def validate(self,validated_data):

        exam_date = validated_data.get("exam_date")

        if exam_date < datetime.today().date():

            raise serializers.ValidationError("invalid date")

        return validated_data

