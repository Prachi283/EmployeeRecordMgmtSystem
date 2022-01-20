from django.db import models
from django.contrib.auth.models import User

class EmployeeDetail(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	empcode=models.CharField(max_length=200)
	empdept=models.CharField(max_length=200,null=True)	
	designation=models.CharField(max_length=200,null=True)
	contact=models.CharField(max_length=200,null=True)
	gender=models.CharField(max_length=200,null=True)
	joiningdate=models.DateField(null=True)

	def __str__(self):
		return self.user.username