from django.test import TestCase
from django.test import Client

class CodeViewTest(TestCase):
	client = Client()
	
	def test_index_response(self):
		response = self.client.get('/')
		self.assertTrue(response.status_code == 200)
	
	def test_index_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'paste/index.html')
	