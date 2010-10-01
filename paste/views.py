from django.shortcuts import render_to_response
from codepaste.paste.models import Code
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django import forms
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

class CodeForm(forms.Form):
	title = forms.CharField(max_length=60)
	language = forms.CharField(max_length=60)
	code = forms.Field(widget=forms.Textarea)

def index(request):
	return render_to_response('paste/index.html', locals(), context_instance=RequestContext(request))
	
def save(request):
	if request.method == 'POST':
		post = request.POST
		title = post['title']
		code = Code(title=post['title'], language=post['language'], code=post['code'])
		code.save()
	return HttpResponseRedirect(reverse('show', args=(code.slug,)))
		
def show(request, slug):
	code = get_object_or_404(Code, slug=slug)
	lexer = get_lexer_by_name(code.language, stripall=True)
	formatter = HtmlFormatter(linenos=True, style='emacs')
	code.code = highlight(code.code, lexer, formatter)

	return render_to_response('paste/show.html', {'code':code}, context_instance=RequestContext(request))