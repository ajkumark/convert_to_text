from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json

from convertorapp.models import Details
from file_convertor import get_captcha


@csrf_exempt
def index(request):
	if request.method == 'POST':
		print request.POST
		print 'files',request.FILES
		print request.POST.get('type', None)
		try:
			file_name = request.FILES['file_name']
		except:
			file_name = request.FILES['0']
		print file_name
		output_text = get_captcha(file_name)
		request_type = request.POST.get('type', None)
		details = Details()
		user = User.objects.get(pk=1)
		details.user = user
		details.file_name = file_name
		details.output_text = output_text
		details.save()
		if request_type == 'mobile':
			print output_text
			return HttpResponse(json.dumps({'data':output_text}))
		return render_to_response('index.html', context_instance=RequestContext(request, {'data':output_text}))
	else:
		return render_to_response('index.html', context_instance=RequestContext(request))
