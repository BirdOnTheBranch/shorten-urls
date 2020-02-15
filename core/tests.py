from django.test import TestCase
from .models import Link
from django.contrib.auth.models import User


class ViewLinks(TestCase):
    def setUp(self):
        Link.objects.create(usuario=User)

    def test_query_in_template(self):
        query_link = Link.objects.filter(usuario=self.request.user)
        self.assertEqual(len(query_link), httpresponse.context['Link'])
