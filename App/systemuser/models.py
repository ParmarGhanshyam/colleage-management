from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SystermUser(models.Model):

    CHOICES = (
        ("student", "Student"),
        ("professor", "Professor")
    )
    CHOICES_Action = (
        ("pending", "Pending"),
        ("active", "Active"),
        ("block", "Blocked"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='systemuser')
    mobile = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=CHOICES_Action, default="pending")
    user_type = models.CharField(max_length=20, choices=CHOICES, default='student')


    def __str__(self):
        return f" {str(self.user)}  ,  {self.mobile}  ,  {self.status}  ,   {self.user_type} "

    class Meta:
        verbose_name_plural = "SystermUser"
