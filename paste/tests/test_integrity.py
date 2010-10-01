from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from codepaste.paste.models import Code
from django.shortcuts import get_object_or_404

class CodeTest(TestCase):
	client = Client()
	
	def test_slugfy(self):
		code = Code(title='title test',language='language',code='code')
		code.save()
		self.assertTrue(code.slug == 'title-test')
	
	def test_paste_code(self):
		self.client.post(reverse('save'), {'title':'test title','language':'python','code':'test_code'})
		code = get_object_or_404(Code, slug='test-title')
		
		self.assertTrue(code)
		
	def test_show_code(self):
		code = Code(title='show test', language='python', code='code show test')
		code.save()
		response = self.client.get(reverse('show', args=(code.slug,)))
		self.assertTrue(response.status_code == 200)
		self.assertContains(response, code.title)