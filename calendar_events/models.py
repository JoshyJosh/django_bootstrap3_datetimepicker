# ruthlessly modified from http://stackoverflow.com/questions/27697939/create-unique-slug-django
from django.db import models
from django.utils.text import slugify

import re


# Create your models here.
class Event(models.Model):
	content = models.TextField(max_length=400, blank=True)
	title = models.CharField(max_length=100, default="Blank Title")
	event_time = models.DateField(auto_now=False)
	slug = models.SlugField(max_length=200, default=slugify("Blank Title"))

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Event, self).save()
		slug_string = slugify(self.title)
		similar_slugs = Event.objects.filter(slug__startswith=slug_string)

		if similar_slugs.count() > 0:
			last_slug = similar_slugs.last().slug
			slug_reg = re.search(r'\d+$', last_slug)
			if slug_reg:
				self.slug = slug_string + "_" +str(int(slug_reg.group(0)) + 1)
			else:
				self.slug = slug_string + "_1"
		else:
			self.slug=slug_string

		super(Event, self).save()
