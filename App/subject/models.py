from django.db import models
from ..sem.models import Semester


class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    sem_name = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='Subject_subject')

    def __str__(self):
        return f" subject name: -  {self.subject_name}   sem: -      {self.sem_name} "

    class Meta:
        verbose_name_plural = "Subject"
