from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from .models import SystermUser
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        # with transaction.atomic():
        username = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['password1']
        mobile = request.POST['mobile']
        address = request.POST['address']

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
        print(user)

    return render(request, 'login.html')
