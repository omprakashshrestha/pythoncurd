from django.db import models


# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=40)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=30)

    class Meta:
        db_table = "employee"
