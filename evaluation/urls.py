from django.urls import path

from evaluation.views import SubmissionStartView

from evaluation.views import SubmissionRetrieveView

from evaluation.views import AnswerCreateView,AnswerUpdateView

urlpatterns=[

    path('assessment/<int:pk>/submission/',SubmissionStartView.as_view()),

    path('submission/<int:pk>/answer/',AnswerCreateView.as_view()),

    path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),

    path('answer/<int:pk>/',AnswerUpdateView.as_view()),
]