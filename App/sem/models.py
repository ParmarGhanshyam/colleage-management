from django.db import models
from ..branch.models import Branch
# Create your models here.


class   Semester(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='Branch_Semester')
    sem_name = models.IntegerField()

    def __str__(self):
        return f" Branch Is :-    {self.branch}   Current Semester is: -  {str(self.sem_name)}"

    class Meta:
        verbose_name_plural = "Semester"
