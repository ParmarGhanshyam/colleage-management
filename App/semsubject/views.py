from django.shortcuts import render,HttpResponse,redirect
from .models import Semstudent
from ..subject.models import Subject
from ..systemuser.models import SystermUser


# Create your views here.
def showstudentinfo(request):
    systemuserdata = SystermUser.objects.get(user_id=request.user)
    semdata = Semstudent.objects.filter(user_id = systemuserdata.id)
    login_user_name = request.user
    datalist = []
    for data in semdata:
        datalist.append(data)
    return render(request,'show_student_info.html',{'datalist':datalist,'systemuser':systemuserdata})


def showstudentsubject(request):
    systemuserdata = SystermUser.objects.get(user_id=request.user)
    semdata = Semstudent.objects.get(user_id = systemuserdata.id)
    print(semdata.sem.id)

    subjectdata = Subject.objects.filter(sem_name = semdata.sem.id)
    datalist = []
    for data in subjectdata:
        datalist.append(data)
    return render(request, 'list_of_subject.html',{'datalist':datalist,'systemuser':systemuserdata})

