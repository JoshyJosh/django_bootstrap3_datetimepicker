import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Event

# Create your tests here.

class EventSlugTest(TestCase):
	def setUp(self):
		Event.objects.create(content="Some test content", title="Some Title", event_time=timezone.now())
		
	def slug_is_created_without_explicit_input(self):
		ev = Event.objects.get(content="Some test content")
		self.assertEqual(ev.slug, "some_content")
