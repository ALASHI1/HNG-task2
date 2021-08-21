from django.db import models
from django.utils import timezone
# Create your models here.

class ContactFormModel(models.Model):
	name = models.CharField(max_length=100)
	contact = models.EmailField()
	purpose = models.TextField()
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.name
