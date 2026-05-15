from django.urls import path
from .views import RegisterView, ConfirmView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('confirm/', ConfirmView.as_view()),
    path('login/', obtain_auth_token),
]