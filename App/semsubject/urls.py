from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views


from . import views
from django.urls import path

app_name = 'semsubject'

urlpatterns = [
    path('showstudentinfo/', views.showstudentinfo, name="showstudentinfo"),
    path('showstudentsubject/', views.showstudentsubject, name="showstudentsubject"),
    path('download_document/<int:pk>', views.download_document, name="downloaddocument"),

]
