from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Task

def home(request):
	return render_to_response('index.html')

def add_acton_to_log(sender, instance, created, **kwargs):
	print sender, instance, created, kwargs, '<--- yooooooo'

# @login_required
def tasks(request):
	order = request.GET.get('o', 'last_updated_on')
	results = Task.objects.filter(created_by=request.user).order_by(order)
	# Put in Pagination
	return render_to_response('tasks.html', {'tasks': results},
		context_instance=RequestContext(request))

