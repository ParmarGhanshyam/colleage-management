from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from .models import SystermUser
from django.contrib import auth
from django.contrib import messages
import hashlib
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import BasePasswordHasher
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        # with transaction.atomic():
        username = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['password1']
        mobile = request.POST['mobile']
        # address = request.POST['address']

        if password == repassword:
            data = User.objects.create_user(username=username, password=password)
            system_user = SystermUser.objects.create(user_id=data.id, mobile=mobile)
            return redirect('teacher_data:login')
        else:
            messages.error(request, "Password does not match")
            return redirect('teacher_data:register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('dropdown')
        user = auth.authenticate(username=username, password=password)
        if user:
            systemuser = SystermUser.objects.get(user=user)
            if systemuser.user_type == user_type:
                if systemuser.user_type == "professor":
                    auth.login(request, user)
                    messages.success(request, "Sucessfully TeacherLogin Done")
                    return redirect('teacher_data:teacher_dashoard')
                else:
                    if systemuser.status == "pending":
                        messages.warning(request, 'Your account Action is Pending.')
                        return redirect('teacher_data:login')
                    elif systemuser.status == "active":
                        auth.login(request, user)
                        messages.success(request, "Sucessfully Login")
                        context = SystermUser.objects.get(user = user)
                        return render(request, 'student_dashboard.html', {'systemuser' : context})
                    else:
                        messages.error(request, "You R Not Authorize for Login ")
                        return redirect('teacher_data:login')
            else:
                messages.warning(request, "You R Selected Wrong User type")
                return redirect('teacher_data:login')
        else:
            messages.error(request, "invalid credentials")
            return redirect('teacher_data:login')
    return render(request, 'login.html')

@login_required(login_url='teacher_data:login')
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required(login_url='teacher_data:login')
def logout_view(request):
    logout(request)
    return redirect('teacher_data:login')


@login_required(login_url='teacher_data:login')
def changepassword(request):
    systemuserdata = SystermUser.objects.get(user_id=request.user)
    print(systemuserdata)
    print(systemuserdata.user)
    data = User.objects.get(username = systemuserdata.user)
    print(data.password)
    hash = hashlib.sha512(data.password.encode()).hexdigest()[:120]
    print(hash)
    if systemuserdata.user:
        auth.login(request,systemuserdata.user)
        if request.method == "POST":
            changepassword = request.POST['changepassword']
            data.set_password(changepassword)
            data.save()
            return redirect('teacher_data:login')

    return render(request,'change_password.html')

@login_required(login_url='teacher_data:login')
def teacher_dashoard(request):
    return render(request, 'teacher_dashboard.html')