from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views


from . import views
from django.urls import path

app_name = 'teacher_data'

urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('student_dashboard/', views.student_dashboard, name="student_dashboard"),
    path('teacher_dashoard/', views.teacher_dashoard, name="teacher_dashoard"),
    path('changepassword/',views.changepassword,name = "changepassword"),
    path('logout/',views.logout_view, name="logout")
]
