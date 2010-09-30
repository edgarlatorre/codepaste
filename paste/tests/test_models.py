from django.test import TestCase
from codepaste.paste.models import Code

class CodeTest(TestCase) :
	def test_should_have_a_title(self) :
		code = Code(language='python',code='code')
		self.assertFalse(self.code_is_valid(code))
	
	def test_should_have_a_language(self):
		code = Code(title='test',code='code')
		self.assertFalse(self.code_is_valid(code))
		
	def test_should_have_a_code(self):
		code = Code(title='test',code='code')
		self.assertFalse(self.code_is_valid(code))
		
	def test_should_have_title_as_unicode(self):
		code = Code(title='title')
		self.assertTrue(str(code) == code.title)
		
	def code_is_valid(self, code) :
		is_valid = True
		try :
			code.save()
		except :
			is_valid = False