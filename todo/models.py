from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	title = models.CharField(max_length=128)
	date_created = models.DateTimeField(auto_now=True)
	is_done = models.BooleanField(default=False)
	content = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title


