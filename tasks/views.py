from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect, HttpResponse

from models import Task
from forms import TaskForm

def home(request):
	return render_to_response('index.html')

def add_acton_to_log(sender, instance, created, **kwargs):
	print sender, instance, created, kwargs, '<--- yooooooo'

# @login_required
def tasks(request):
	"""Lists tasks"""
	if request.method == 'GET':
		order = request.GET.get('o', 'last_updated_on')
		results = Task.objects.filter(created_by=request.user).order_by(order)
		# Put in Pagination
		return render_to_response('tasks.html', {'tasks': results},
			context_instance=RequestContext(request))

	# post
	task = TaskForm(request.POST)
	if task.is_valid():
		task.save()
		return HttpResponseRedirect('/task/%d'%task.id)
	return HttpResponse(status=400)

def task_detail(request, task_id):
	"""Creates/Deletes/Modifies Tasks"""
	task = Task.objects.filter(id=task_id)
	print task
	if not task:
		return Http404()


