from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path

from .views import Register,ChangePasswordUpdate

app_name = 'teacher_data'

default_router = DefaultRouter()

default_router.register('',Register,basename='register')
default_router.register('change_password',ChangePasswordUpdate,basename='change_password')

urlpatterns = [
    # path('', Register.as_view(), name="register"),
    path('',include(default_router.urls)),
    # path('login/', views.login, name="login"),
    path('student_dashboard/', views.student_dashboard, name="student_dashboard"),
    path('teacher_dashoard/', views.teacher_dashoard, name="teacher_dashoard"),
    # path('changepassword/',views.changepassword,name = "changepassword"),
    # path('logout/',views.logout_view, name="logout")
]
