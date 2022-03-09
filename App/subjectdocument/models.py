from django.db import models
from ..subject.models import Subject
from django.contrib.auth.models import User
from ..systemuser.models import SystermUser



class SubjectDocument(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='SubjectDocument_Subject')
    user = models.ForeignKey(SystermUser, on_delete=models.CASCADE, related_name='SubjectDocument_user')
    filefield = models.FileField(upload_to='Document/')
    filename = models.CharField(max_length=30)

    def __str__(self):
        return f"   {str(self.subject)}    {str(self.user)}  {str(self.filefield)}   {str(self.filename)}"

    class Meta:
        verbose_name_plural = "SubjectDocument"
