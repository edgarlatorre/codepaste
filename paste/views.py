from django.shortcuts import render_to_response
from codepaste.paste.models import Code
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django import forms

class CodeForm(forms.Form):
	title = forms.CharField(max_length=60)
	language = forms.CharField(max_length=60)
	code = forms.Field(widget=forms.Textarea)

def index(request):
	return render_to_response('paste/index.html', locals(), context_instance=RequestContext(request))
	
def save(request):
	"""docstring for save"""
	pass

