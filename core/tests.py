from django.test import TestCase, Client
from .models import Link, User
from .forms import UrlForm
from django.urls import reverse


class ViewLinks(TestCase):
    def setUp(self):
        self.query=Link.objects.create( url="https://www.youtube.com/watch?v=dlWd8J1gc48&t=331s", code="WcegF")
        self.query2=Link.objects.create( url="https://www.marca.com/futbol/barcelona/2020/01/29/5e31a207ca4741836a8b45a3.html", code="HpweB")


    def test_for_invalid_input_renders_home_template(self):
        response = self.client.post('/', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    
    def test_invalid_url(self):
        response = self.client.post('/invalid/', data={'text': ''})
        self.assertEqual(response.status_code, 404)


    def test_instance_in_database(self):
        instance=Link.objects.filter(code="WcegF")
        self.assertIs(instance, self.query)


    def test_view_context(self):
        name_form = UrlForm
        response = self.client.get(reverse("home_view"))
        self.assertIsInstance(response.context['form'], UrlForm)