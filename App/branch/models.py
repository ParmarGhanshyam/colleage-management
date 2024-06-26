from django.db import models

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name_plural = "Branch"
        db_table = "Field-Branch"
