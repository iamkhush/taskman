from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
	STATUS_CHOICES = (
			(1, 'Completed'),
			(2, 'InCompleted'),
			(3, 'Deleted')
		)
	name = models.CharField(max_length=200)
	status = models.IntegerField(choices=STATUS_CHOICES, default=2)
	deadline = models.DateTimeField()
	added_on = models.DateTimeField(auto_now_add=True)
	last_updated_on = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User)

	def __unicode__(self):
		return self.name

class ActionLog(models.Model):
	added_on = models.DateTimeField(auto_now_add=True)
	description = models.TextField()