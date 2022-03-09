from django.db import models
from ..sem.models import Semester
from django.contrib.auth.models import User
from ..systemuser.models import SystermUser

# Create your models here.


class Semstudent(models.Model):
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='Semsstudent_Semester')
    user = models.ForeignKey(SystermUser, on_delete=models.CASCADE, related_name='semstudent_User')


    def __str__(self):
        return f"   {str(self.sem)}    {str(self.user)} "

    class Meta:
        verbose_name_plural = "Semstudent"

