from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

from . import views
from django.urls import path

app_name = 'subjectdocument'

urlpatterns = [
    path('list_document/', views.list_document, name="listdocument"),
    path('add_data/<int:pk>/', views.add_data, name="adddata"),
    path('add_document/<int:pk>/',views.add_document,name = 'adddocument'),
]
