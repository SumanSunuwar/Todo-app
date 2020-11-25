from django.db import models
from django.contrib.auth.models import User

#from userprofile.models import Profile

# Create your models here.
#Let's create an object > Todo object
# fields : title , description, date
class Todo(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	date = models.DateField(null=True,blank=True)
	todo_image = models.ImageField(upload_to="upload/todo",blank=True, null=True)
	is_greater_priority = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title	
 