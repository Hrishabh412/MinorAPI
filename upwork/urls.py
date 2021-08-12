
from django.urls import path
from .views import  student_detail,  StudentGenericAPIView

urlpatterns = [
    path('student_details/<int:pk>', student_detail),
    path('student/', StudentGenericAPIView.as_view()),
    
]