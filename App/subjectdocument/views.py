from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import SubjectDocument
from ..subject.models import Subject
from ..systemuser.models import SystermUser
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import SubjectDocumentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticated,)
def list_document(request):
    systemuserdata = SystermUser.objects.get(user_id=request.user)
    print(systemuserdata.user.pk)
    context = SubjectDocument.objects.filter(user=systemuserdata).distinct('subject')
    # datas = SubjectDocument.order_by('blog').distinct('blog')
    # datas = SubjectDocument.order_by('context.subject.subject_name').distinct('context.subject.subject_name')
    datalist = []
    for data in context:
        datalist.append(data)
        print(data)

    return render(request, 'list_document.html', {'subjects': datalist})

@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticated,)
def add_data(request, pk):
    systemuserdata = SystermUser.objects.get(user_id=request.user)
    print(systemuserdata.user.pk)
    context = SubjectDocument.objects.filter(subject_id=pk)

    datalist = []
    for data in context:
        datalist.append(data)
        print(data)
    return render(request, 'add_data.html', {'subjects': datalist})

@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticated,)
def add_document(request, pk):
    if request.method == "POST":
        systemuserdata = SystermUser.objects.get(user_id=request.user)
        # print(systemuserdata.user.pk)
        context = SubjectDocument.objects.get(id=pk)
        filedocument = request.POST['myfile']
        filename = request.POST['filename']
        subjectdocumnet = SubjectDocument.objects.create(subject=context.subject, user=systemuserdata,
                                                         filefield=filedocument, filename=filename)
        return redirect("subjectdocument:adddata", pk=context.subject.id)

    else:
        systemuserdata = SystermUser.objects.get(user_id=request.user)
        # print(systemuserdata.user.pk)
        context = SubjectDocument.objects.get(id=pk)
        return render(request, 'add_document.html', {'data': context})
