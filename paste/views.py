from django.shortcuts import render_to_response
from codepaste.paste.models import Code
from django.template import RequestContext
from django.shortcuts import get_object_or_404

def index(request):
	return render_to_response('paste/index.html')

