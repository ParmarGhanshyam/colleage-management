from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path
from .views import ShowStudentInfo

app_name = 'semsubject'
default_router = DefaultRouter()

default_router.register('listalldata',ShowStudentInfo,basename='ShowStudentInfo')

urlpatterns = [
    # path('showstudentinfo/', views.showstudentinfo, name="showstudentinfo"),
    # path('showstudentsubject/', views.showstudentsubject, name="showstudentsubject"),
    # path('download_document/<int:pk>', views.download_document, name="downloaddocument"),

]
