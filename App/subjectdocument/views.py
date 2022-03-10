from django.shortcuts import render
from .models import SubjectDocument
from ..subject.models import Subject
from ..systemuser.models import SystermUser
# Create your views here.


def list_document(request):
    systemuserdata = SystermUser.objects.get(user_id = request.user)
    print(systemuserdata.user.pk)
    context = SubjectDocument.objects.filter(user = systemuserdata)
    datalist = []
    for data in context:
        datalist.append(data)
        print(data)
    return render(request, 'list_document.html',{'subjects':datalist})


def add_data(request,pk):
    systemuserdata = SystermUser.objects.get(user_id = request.user)
    print(systemuserdata.user.pk)
    context = SubjectDocument.objects.filter(id = pk)

    datalist = []
    for data in context:
        datalist.append(data)
        print(data)
    return render(request, 'add_data.html',{'subjects':datalist})


def add_document(request):
    systemuserdata = SystermUser.objects.get(user_id = request.user)


    return render(request, 'add_document.html')

