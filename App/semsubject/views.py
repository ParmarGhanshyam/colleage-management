from django.shortcuts import render,HttpResponse,redirect
from .models import Semstudent

from ..systemuser.models import SystermUser


# Create your views here.
def showstudentinfo(request):
    systemuserdata = SystermUser.objects.get(user_id=request.user)
    print(systemuserdata.id)
    semdata = Semstudent.objects.filter(user_id = systemuserdata.id)
    login_user_name = request.user
    datalist = []
    for data in semdata:
        datalist.append(data)
    return render(request,'show_student_info.html',{'datalist':datalist,'systemuser':systemuserdata})


# def showstudentsubject(request):
#