from django.urls import path

from problem.views import QuestionCreateView,QuestionRetrieveUpdateDeleteView

urlpatterns=[

    path('assessment/<int:pk>/question/',QuestionCreateView.as_view()),

    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),

]