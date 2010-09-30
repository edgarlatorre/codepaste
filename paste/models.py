from django.db import models

class Code(models.Model):
	title = models.CharField(max_length=60)
	language = models.CharField(max_length=60)
	code = models.TextField()
	
	def __unicode__(self):
		return self.title
