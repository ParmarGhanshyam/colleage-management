from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from .models import SystermUser
from django.contrib import auth
from .serializer import UserSerializer
from django.contrib import messages
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import hashlib
from django.contrib.auth.decorators import login_required
from rest_framework import mixins
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import BasePasswordHasher
from django.contrib.auth import logout
from rest_framework.response import Response
from .serializer import SystermUserSerializer
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin
# Create your views here.
class Register(CreateModelMixin,GenericViewSet):
    serializer_class = SystermUserSerializer
    queryset = SystermUser.objects.all()
    permission_classes = []
    authentication_classes = []

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "username" : self.request.data.get('username'),
                "password" : self.request.data.get('password')
            }
        )
        return context


class ChangePasswordUpdate(UpdateModelMixin,GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# @api_view(['GET', 'POST'])
# def register(request):
#     if request.method == 'POST':
#         # with transaction.atomic():
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repassword = request.POST.get('password1')
#         mobile = request.POST.get('mobile')
#         # address = request.POST['address']
#
#         if password == repassword:
#             user_instance = User.objects.create_user(username=username, password=password)
#             # system_user = SystermUser.objects.create(user_id=data.id, mobile=mobile)
#             request_post = request.data.copy()
#             request_post['user'] = user_instance.id
#             system_user_serializer = SystermUserSerializer(data =request_post)
#             if system_user_serializer.is_valid():
#                 system_user_instance = system_user_serializer.save()
#                 return Response(SystermUserSerializer(instance=system_user_instance).data, status=status.HTTP_201_CREATED)
#             else:
#                 print(system_user_serializer.errors)
#                 return  Response(system_user_serializer.errors)
#
#     #         return redirect('teacher_data:login')
#     #     else:
#     #         messages.error(request, "Password does not match")
#     #         return redirect('teacher_data:register')
#     #
#     # return render(request, 'register.html')

# @api_view(['GET', 'POST'])
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         user_type = request.POST.get('dropdown')
#         user = auth.authenticate(username=username, password=password)
#         if user:
#             systemuser = SystermUser.objects.get(user=user)
#             if systemuser.user_type == user_type:
#                 if systemuser.user_type == "professor":
#                     auth.login(request, user)
#                     messages.success(request, "Sucessfully TeacherLogin Done")
#                     return redirect('teacher_data:teacher_dashoard')
#                 else:
#                     if systemuser.status == "pending":
#                         messages.warning(request, 'Your account Action is Pending.')
#                         return redirect('teacher_data:login')
#                     elif systemuser.status == "active":
#                         auth.login(request, user)
#                         messages.success(request, "Sucessfully Login")
#                         context = SystermUser.objects.get(user = user)
#                         return render(request, 'student_dashboard.html', {'systemuser' : context})
#                     else:
#                         messages.error(request, "You R Not Authorize for Login ")
#                         return redirect('teacher_data:login')
#             else:
#                 messages.warning(request, "You R Selected Wrong User type")
#                 return redirect('teacher_data:login')
#         else:
#             messages.error(request, "invalid credentials")
#             return redirect('teacher_data:login')
#     return render(request, 'login.html')


@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticated,)
def student_dashboard(request):
    return render(request, 'student_dashboard.html')



# @api_view(['GET', 'POST'])
# @permission_classes(IsAuthenticated,)
# def logout_view(request):
#     logout(request)
#     return redirect('teacher_data:login')



# @api_view(['GET', 'POST'])
# @permission_classes(IsAuthenticated,)
# def changepassword(request):
#     systemuserdata = SystermUser.objects.get(user_id=request.user)
#     print(systemuserdata)
#     print(systemuserdata.user)
#     data = User.objects.get(username = systemuserdata.user)
#     print(data.password)
#     hash = hashlib.sha512(data.password.encode()).hexdigest()[:120]
#     print(hash)
#     if systemuserdata.user:
#         auth.login(request,systemuserdata.user)
#         if request.method == "POST":
#             changepassword = request.POST['changepassword']
#             data.set_password(changepassword)
#             data.save()
#             return redirect('teacher_data:login')
#
#     return render(request,'change_password.html')



@api_view(['GET', 'POST'])
def teacher_dashoard(request):
    return render(request, 'teacher_dashboard.html')