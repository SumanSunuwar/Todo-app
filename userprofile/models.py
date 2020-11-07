from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255, blank=True)
	middle_name = models.CharField(max_length=255, blank=True)
	last_name = models.CharField(max_length=255, blank=True)
	contact = models.CharField(max_length=255, blank=True)
	address = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.first_name	


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)