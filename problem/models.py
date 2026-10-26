from django.db import models

from exam.models import Assessment

from accounts.models import User

# Create your models here.
class Question(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    score = models.PositiveIntegerField()

    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE)

    sample_input = models.TextField(null=True)

    sample_output = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    question_number = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):

        last_question_object = Question.objects.filter(assessment=self.assessment).last()

        if last_question_object:

            self.question_number = last_question_object.question_number+1

        else:

            self.question_number = 1

        return super().save(*args,**kwargs)

