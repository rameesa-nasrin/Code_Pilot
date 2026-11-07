from django.urls import path

from accounts.views import AdminCreateView,StudentCreateView

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import ProfileUpdateView

from accounts.views import ProfileDetailView

urlpatterns=[

    path("admin/register/",AdminCreateView.as_view()),

    path('student/register/',StudentCreateView.as_view()),

    path('jwt/token/',TokenObtainPairView.as_view()),

    path('jwt/token/refresh/',TokenRefreshView.as_view()),

    path('profile/complete/',ProfileUpdateView.as_view()),

    path('profile/me/',ProfileDetailView.as_view()),
]