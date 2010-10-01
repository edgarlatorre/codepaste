from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

class CodeViewTest(TestCase):
	client = Client()
	
	def test_index_response(self):
		response = self.client.get('/')
		self.assertTrue(response.status_code == 200)
	
	def test_index_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'paste/index.html')
			
	def test_should_contain_a_form(self):
		response = self.client.get('/')
		self.assertContains(response, '<form')
		self.assertContains(response, '</form>')
		
	def test_should_contain_a_title_field(self):
		response = self.client.get('/')
		self.assertContains(response, "id='title'")
		
	def test_should_contain_a_language_field(self):
		response = self.client.get('/')
		self.assertContains(response, "id='language'")
		
	def test_should_contain_a_code_field(self):
		response = self.client.get('/')
		self.assertContains(response, "id='code'")
		
	def test_should_contain_a_submit_button(self):
		response = self.client.get('/')
		self.assertContains(response, "type='submit'")