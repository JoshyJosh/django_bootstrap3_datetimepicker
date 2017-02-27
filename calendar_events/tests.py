import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Event

# Create your tests here.


class EventSlugTest(TestCase):
	def setUp(self):
		Event.objects.create(content="Some test content", title="Some Title", event_time=timezone.now())
		Event.objects.create(content="Different content", title="Some Title", event_time=timezone.now())

	def test_slug_is_created_without_explicit_input(self):
		ev = Event.objects.get(content="Some test content")
		self.assertEqual(ev.slug, "some-title")

	def test_slug_is_created_and_incremented_if_already_used(self):
		ev1 = Event.objects.get(content="Some test content")
		ev2 = Event.objects.get(content="Different content")
		self.assertEqual(ev1.slug, "some-title")
		self.assertEqual(ev2.slug, "some-title_1")
