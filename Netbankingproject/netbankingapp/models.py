from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.


class department(models.Model):
    departmentname = models.CharField(max_length=100)


class employee(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField()
    deptid = models.ForeignKey(department, on_delete=CASCADE)
    empname = models.CharField(max_length=100)
    address = models.CharField(max_length=500, null=True)
    contactno = models.CharField(max_length=20)
    def __str__(self):
        return self.name