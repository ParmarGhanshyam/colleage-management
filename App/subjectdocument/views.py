from django.shortcuts import render,redirect,reverse
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


def add_document(request,pk):
    if request.method == "POST":
        systemuserdata = SystermUser.objects.get(user_id = request.user)
        # print(systemuserdata.user.pk)
        context = SubjectDocument.objects.get(id = pk)
        filedocument = request.POST['myfile']
        filename = request.POST['filename']
        subjectdocumnet = SubjectDocument.objects.create(subject=context.subject,user = systemuserdata,filefield = filedocument, filename=filename)
        return redirect(reverse('subjectdocument:adddata data.subject.id'))
        # return render(request, 'add_document.html',{'data':context})
    else:
        systemuserdata = SystermUser.objects.get(user_id = request.user)
        # print(systemuserdata.user.pk)
        context = SubjectDocument.objects.get(id = pk)
        return render(request, 'add_document.html',{'data':context})

