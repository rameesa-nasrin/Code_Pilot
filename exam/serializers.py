from rest_framework import serializers

from django.db.models import Sum

from exam.models import Assessment

from  problem.models import Question

from problem.serializers import QuestionSerializer

from accounts.models import User

from datetime import datetime


class AssessmentSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    greetings = serializers.SerializerMethodField(read_only=True)

    question_count = serializers.SerializerMethodField(read_only=True)

    total_marks = serializers.SerializerMethodField(read_only=True)

    questions = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Assessment

        fields = "__all__"

        read_only_fields = ["id","end_time","created_by"]

    def validate(self,validated_data):

        exam_date = validated_data.get("exam_date")

        if exam_date < datetime.today().date():

            raise serializers.ValidationError("invalid date")

        return validated_data

    def get_greetings(self,obj):

        return "good morning"

    def get_question_count(self,obj):

        return Question.objects.filter(assessment=obj).count()

    def get_total_marks(self,obj):

        return Question.objects.filter(assessment=obj).values("score").aggregate(total=Sum("score")).get("total")

    def get_questions(self,obj):

        question_objects = Question.objects.filter(assessment=obj)

        serializer_instance = QuestionSerializer(question_objects,many=True)

        return serializer_instance.data