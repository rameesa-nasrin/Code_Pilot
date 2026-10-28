from django.db import models
from django.conf import settings
from django.utils import timezone

from exam.models import Assessment

class Submission(models.Model):

    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('evaluated', 'Evaluated'),
    )

    EVALUATION_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='submissions')
    
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    
    started_at = models.DateTimeField(auto_now_add=True)
    
    submitted_at = models.DateTimeField(null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    
    evaluation_status = models.CharField(max_length=20, choices=EVALUATION_STATUS_CHOICES, default='pending')
    
    total_marks = models.IntegerField(default=0)  # Calculated after evaluation
    
    max_marks = models.IntegerField(default=0)    # Populated from questions total

    class Meta:

        unique_together = ('assessment', 'student')  # One submission per student per assessment

    def __str__(self):

        return f"{self.student.username} - {self.assessment.title} ({self.status})"


class Answer(models.Model):

    
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='answers')
    
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
    
    answer_text = models.TextField()
    
    marks_awarded = models.IntegerField(null=True, blank=True)
    
    feedback = models.TextField(null=True, blank=True)
    
    evaluated_at = models.DateTimeField(null=True, blank=True)

    class Meta:

        unique_together = ('submission','question')  # One answer per question per submission

    def __str__(self):
        
        return f"Answer to Q{self.question.id} for Submission {self.submission.id}"