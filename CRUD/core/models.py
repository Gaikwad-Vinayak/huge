from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Designation_Mst(models.Model):
    designaton = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class Employee_Mst(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    designationld=models.ForeignKey(Designation_Mst,on_delete=models.CASCADE,default='select')
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    date_of_joining = models.DateField()
    salary = models.FloatField()

    def __str__(self):
        return str(self.id)







