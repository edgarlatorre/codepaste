from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

class Code(models.Model):
	title = models.CharField(max_length=60, unique=True)
	language = models.CharField(max_length=60)
	code = models.TextField()
	slug = models.SlugField(max_length=100)
	
	def __unicode__(self):
		return self.title
		
def code_pre_save(signal, instance, sender, **kwargs):
	instance.slug = slugify(instance.title)
	
signals.pre_save.connect(code_pre_save, sender=Code)
	