from django.urls import path

from exam.views import AssessmentListView 
from exam.views import AssessmentCreateView
from exam.views import AssessmentRetrieveUpdateView

urlpatterns=[

    path('all/',AssessmentListView.as_view()),

    path('add/',AssessmentCreateView.as_view()),

    path('<int:pk>/',AssessmentRetrieveUpdateView.as_view()),

]
