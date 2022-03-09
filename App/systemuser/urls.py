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

]