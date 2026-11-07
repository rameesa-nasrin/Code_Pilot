from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = {
        ("student","student"),
        ("admin","admin")
    }

    role = models.CharField(max_length=100,choices=ROLE_CHOICES,default="student")



class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=20,null=True)

    github_url = models.URLField(null=True)

    linkedin_url = models.URLField(null=True) 

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")



from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)



from django.core.mail import send_mail

def send_invitation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        send_mail(
                "account creation confirmation",
                "you have successfully created user in codepilot application",
                "rameesarahima@gmail.com",
                ["safnaaboobacker05@gmail.com"],
                )
        
post_save.connect(send_invitation_mail,sender=User)        