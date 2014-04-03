from django.forms import ModelForm
from models import Task

class TaskForm(ModelForm):
	model = Task
