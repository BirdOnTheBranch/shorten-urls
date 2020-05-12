from django.test import TestCase, Client
from .models import Link
from django.contrib.auth import get_user_model



class ViewLinks(TestCase):
    def setUp(self):
        """ Create active user """
        UserModel = get_user_model()
        self.user = UserModel.objects.create_user('wane', 'wane@a.com', 'wane')
        

    def test_for_invalid_input_renders_home_template(self):
        """ Invalids users in template """
        user_request = self.client.post('/', data={'url': '456367'})
        self.assertEqual(user_request.status_code, 200)
        self.assertTemplateUsed(user_request, 'core/home.html')

    
    def test_invalid_url(self):
        """ Returns for "/invalid" url, error 404 """
        user_request = self.client.post('/invalid/')
        self.assertEqual(user_request.status_code, 404)
       

    def test_code_of_user_login_in_template(self):
        """ Generate short code for loged user in template """
        Link.objects.create(code="WcegF", usuario=self.user)
        self.client.login(username='wane', password='wane')
        user_request = self.client.get('/')
        self.assertContains(user_request, 'WcegF')


    def test_generated_url_assigned_to_the_user(self):
        """ Imput url in template registered in data base """
        self.client.login(username='wane', password='wane')
        user_request = self.client.post('/', data={'url': 'http://www.google.com'})
        genereated_url = Link.objects.get(url="http://www.google.com")
        self.assertContains(user_request, genereated_url.url)
        self.assertEqual(self.user, genereated_url.usuario)


    def test_url_not_passed(self):
        """ If post input url is None return 'invalid URL' in message """
        user_request = self.client.post('/', data={'url': ''})
        self.assertContains(user_request, "Invalid URL")


    def test_wrong_url(self):
        """ If post input url is not valid, return 'invalid URL' in message """
        user_request = self.client.post('/', data={'url': 'tomate'})
        self.assertContains(user_request, "Invalid URL")


    def test_saved_if_not_logged(self):
        """ For user not registered url is saved in data base """
        self.client.post('/', data={'url':'http://www.google.com'})
        links = Link.objects.all()
        self.assertEqual(1, len(links))
        genereated_code = Link.objects.get(url="http://www.google.com")
        self.assertIsNone(genereated_code.usuario)
        