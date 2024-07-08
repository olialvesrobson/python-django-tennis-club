from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=20)
  lastname = models.CharField(max_length=55)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField()
  active = models.BooleanField(default=True)