from django.db import models
from account.models import CustomUser

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=250)
    salary = models.FloatField()
    linkedin = models.URLField()
    supervisor = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
    related_name='sub_ordinates')
    department = models.CharField(max_length=350)
    employee_num = models.CharField(max_length=6, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length=250)
    salary = models.FloatField()
    linkedin = models.URLField()
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
    related_name='employee')
    department = models.CharField(max_length=350)
    company_num = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.name